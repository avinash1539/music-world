# Generated by Django 3.0.7 on 2020-07-11 06:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='User_details',
        ),
    ]
