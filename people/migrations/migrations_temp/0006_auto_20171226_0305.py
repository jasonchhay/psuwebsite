# Generated by Django 2.0 on 2017-12-26 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20171226_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='image',
            field=models.ImageField(default='professor_portraits/noimage.png', upload_to='professor_portraits/'),
        ),
    ]
