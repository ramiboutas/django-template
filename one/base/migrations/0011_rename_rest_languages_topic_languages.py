# Generated by Django 5.1.4 on 2025-01-26 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_remove_topic_languages_topic_rest_languages"),
    ]

    operations = [
        migrations.RenameField(
            model_name="topic",
            old_name="rest_languages",
            new_name="languages",
        ),
    ]
