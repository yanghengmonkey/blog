# Generated by Django 2.1.4 on 2019-01-05 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_log',
            new_name='album_logo',
        ),
    ]
