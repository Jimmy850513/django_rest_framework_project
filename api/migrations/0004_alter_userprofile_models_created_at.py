# Generated by Django 5.0.7 on 2024-07-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_userprofile_userprofile_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile_models',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
