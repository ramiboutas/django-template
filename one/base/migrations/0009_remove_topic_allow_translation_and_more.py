# Generated by Django 5.1.4 on 2025-01-26 09:01

import one.base.utils.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_delete_traffic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="topic",
            name="allow_translation",
        ),
        migrations.RemoveField(
            model_name="topic",
            name="override_translated_fields",
        ),
        migrations.AddField(
            model_name="topic",
            name="default_language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("de", "German"),
                    ("es", "Spanish"),
                    ("fr", "French"),
                    ("el", "Greek"),
                    ("it", "Italian"),
                    ("nl", "Dutch"),
                    ("pl", "Polish"),
                    ("pt", "Portuguese"),
                    ("ru", "Russian"),
                    ("sk", "Slovak"),
                    ("sl", "Slovenian"),
                    ("sv", "Swedish"),
                    ("tr", "Turkish"),
                    ("uk", "Ukrainian"),
                ],
                default="en",
                max_length=4,
            ),
        ),
        migrations.AddField(
            model_name="topic",
            name="languages",
            field=one.base.utils.db_fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("en", "English"),
                        ("de", "German"),
                        ("es", "Spanish"),
                        ("fr", "French"),
                        ("el", "Greek"),
                        ("it", "Italian"),
                        ("nl", "Dutch"),
                        ("pl", "Polish"),
                        ("pt", "Portuguese"),
                        ("ru", "Russian"),
                        ("sk", "Slovak"),
                        ("sl", "Slovenian"),
                        ("sv", "Swedish"),
                        ("tr", "Turkish"),
                        ("uk", "Ukrainian"),
                    ],
                    max_length=4,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]
