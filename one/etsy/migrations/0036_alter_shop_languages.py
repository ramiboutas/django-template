# Generated by Django 5.1.4 on 2025-02-18 22:23

import one.base.utils.db_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("etsy", "0035_shop_shop_dict"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="languages",
            field=one.base.utils.db_fields.ChoiceArrayField(
                base_field=models.CharField(max_length=16), default=[], size=None
            ),
        ),
    ]
