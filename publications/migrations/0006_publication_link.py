# Generated by Django 2.0.6 on 2018-07-09 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20180709_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
