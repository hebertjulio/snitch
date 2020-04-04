from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.dateparse import parse_datetime
from django.utils import timezone

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from ...models import Package, Release


class GithubInterface(object):
    query = '''{
        repository(owner: "%s", name: "%s") {
            tags:refs(refPrefix: "refs/tags/", first: 10, orderBy: {
            field: TAG_COMMIT_DATE, direction: DESC}) {
                nodes {
                    name
                    target {
                        ... on Commit {
                            author {
                                date
                            }
                        },
                        ... on Tag {
                            tagger {
                                date
                            }
                        }
                    }
                }
            }
        }
    }'''

    def __init__(self):
        access_token = settings.CODE_HOSTINGS['github']['ACCESS_TOKEN']
        transport = RequestsHTTPTransport(
            url='https://api.github.com/graphql',
            use_json=True,
            headers={
                'Authorization': 'bearer %s' % access_token,
                'Content-type': 'application/json',
            },
            verify=True
        )
        self.client = Client(
            retries=3,
            transport=transport,
            fetch_schema_from_transport=True
        )

    def get_releases(self, repository_owner, repository_name):
        query = gql(self.query % (repository_owner, repository_name))
        releases = self.client.execute(query)
        for release in releases['repository']['tags']['nodes']:
            name = release['name']
            created = parse_datetime(
                release['target']['author']['date']
                if 'author' in release['target']
                else release['target']['tagger']['date']
            )
            yield {
                'name': name,
                'created': created,
            }


CODE_HOSTINGS = {
    'github': GithubInterface(),
}


class Command(BaseCommand):
    help = 'Watch for new releases in code hosting.'

    def handle(self, *args, **options):
        for package in Package.objects.all():
            code_hosting = CODE_HOSTINGS[package.code_hosting]
            releases = code_hosting.get_releases(
                package.repository_owner, package.repository_name)
            self.add_release(releases, package)

    def add_release(self, releases, package):
        now = timezone.now()
        for release in releases:
            if abs(now - release['created']).days <= 10:
                release_exists = Release.objects.filter(
                    name=release['name'], package=package
                ).exists()
                if release_exists is False:
                    Release.objects.create(**{
                        **release, 'package': package
                    })
