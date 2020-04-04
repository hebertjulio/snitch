# Generated by Django 3.0.4 on 2020-04-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='body',
        ),
        migrations.AddField(
            model_name='package',
            name='programming_language',
            field=models.CharField(choices=[('python', 'Python'), ('javascript', 'JavaScript')], default='', max_length=30, verbose_name='programming language'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='log',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='object id'),
        ),
        migrations.AlterField(
            model_name='package',
            name='code_hosting',
            field=models.CharField(choices=[('github', 'GitHub')], max_length=30, verbose_name='code hosting'),
        ),
        migrations.AlterField(
            model_name='package',
            name='twitter_account',
            field=models.CharField(choices=[('pypackages', 'PyPackages')], max_length=30, verbose_name='twitter account'),
        ),
        migrations.AlterUniqueTogether(
            name='package',
            unique_together={('code_hosting', 'repository'), ('name', 'programming_language')},
        ),
        migrations.RemoveField(
            model_name='package',
            name='technology',
        ),
    ]