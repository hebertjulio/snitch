# Generated by Django 3.0.4 on 2020-04-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0016_auto_20200413_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['status', '-created'], 'verbose_name': 'release', 'verbose_name_plural': 'releases'},
        ),
        migrations.RemoveField(
            model_name='package',
            name='code_hosting_repository',
        ),
        migrations.RemoveField(
            model_name='package',
            name='release_regex',
        ),
        migrations.RemoveField(
            model_name='package',
            name='site_url',
        ),
        migrations.RemoveField(
            model_name='package',
            name='source',
        ),
        migrations.RemoveField(
            model_name='package',
            name='tags',
        ),
        migrations.AddField(
            model_name='package',
            name='homepage',
            field=models.CharField(default='', max_length=255, verbose_name='homepage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='keywords',
            field=models.CharField(default='', max_length=255, verbose_name='keywords'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='repository',
            field=models.CharField(blank=True, max_length=200, verbose_name='repository'),
        ),
        migrations.AddField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('done', 'done')], db_index=True, default='new', max_length=50, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.CharField(max_length=255, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='package',
            name='programming_language',
            field=models.CharField(choices=[('python', 'python')], max_length=50, verbose_name='programming language'),
        ),
    ]