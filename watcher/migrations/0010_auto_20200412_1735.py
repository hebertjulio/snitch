# Generated by Django 3.0.4 on 2020-04-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0009_auto_20200410_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='source_id',
            field=models.CharField(default='', max_length=200, verbose_name='source id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='source_type',
            field=models.CharField(choices=[('github', 'github'), ('pypi', 'pypi')], default='github', max_length=50, verbose_name='source type'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='package',
            unique_together={('name', 'programming_language')},
        ),
        migrations.RemoveField(
            model_name='package',
            name='code_hosting',
        ),
    ]
