# Generated by Django 5.0.7 on 2024-07-24 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userprofile_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserProfile_models',
        ),
    ]