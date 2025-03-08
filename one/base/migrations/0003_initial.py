# Generated by Django 5.1.4 on 2024-12-19 19:34

import auto_prefetch
import django.db.models.deletion
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    # initial = True

    dependencies = [
        ("base", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="traffic",
            name="user",
            field=auto_prefetch.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
