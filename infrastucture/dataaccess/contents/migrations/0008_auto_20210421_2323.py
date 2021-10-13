# Generated by Django 2.2.3 on 2021-04-22 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contents', '0007_auto_20210412_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='sections',
            field=models.ManyToManyField(related_name='posts', through='contents.PostSettings', to='contents.Section'),
        ),
        migrations.AlterField(
            model_name='section',
            name='pages',
            field=models.ManyToManyField(related_name='sections', through='contents.SectionSelector', to='contents.Page'),
        ),
    ]
