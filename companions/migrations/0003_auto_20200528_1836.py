# Generated by Django 2.2.6 on 2020-05-28 17:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companions', '0002_auto_20200528_0827'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserProfileModel',
        ),
    ]
