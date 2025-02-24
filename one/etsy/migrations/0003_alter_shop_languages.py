# Generated by Django 5.1.4 on 2025-01-26 09:12

from django.db import migrations, models

import one.base.utils.db


class Migration(migrations.Migration):

    dependencies = [
        ("etsy", "0002_remove_shop_allow_translation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="languages",
            field=one.base.utils.db.ChoiceArrayField(
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
                    max_length=8,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]
