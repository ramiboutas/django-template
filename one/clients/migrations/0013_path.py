# Generated by Django 5.1.4 on 2024-12-29 01:50

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0012_rename_autoblockpath_spampath"),
    ]

    operations = [
        migrations.CreateModel(
            name="Path",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=256, unique=True)),
                ("is_spam", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
