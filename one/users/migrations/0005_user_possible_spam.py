# Generated by Django 5.1.4 on 2025-02-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_sites"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="possible_spam",
            field=models.BooleanField(default=False),
        ),
    ]
