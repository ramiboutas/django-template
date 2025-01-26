# Generated by Django 5.1.4 on 2025-01-26 10:07

import one.base.utils.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0027_site_page_description_site_page_description_de_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="rest_languages",
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
                    max_length=8,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]
