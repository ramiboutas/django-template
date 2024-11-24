# Generated by Django 5.1.3 on 2024-11-24 11:44

import django.contrib.sites.models
import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0015_rename_languages_extendedsite_rest_languages_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="extendedsite",
            options={"base_manager_name": "prefetch_manager"},
        ),
        migrations.AlterModelManagers(
            name="extendedsite",
            managers=[
                ("objects", django.contrib.sites.models.SiteManager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
