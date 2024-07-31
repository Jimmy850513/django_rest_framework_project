# Generated by Django 5.0.7 on 2024-07-25 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_userprofile_models_is_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModels',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=150)),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile_models')),
            ],
        ),
    ]