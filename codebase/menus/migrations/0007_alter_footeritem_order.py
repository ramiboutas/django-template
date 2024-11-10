# Generated by Django 5.1.3 on 2024-11-10 11:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0006_alter_socialmedialink_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footeritem",
            name="order",
            field=models.PositiveSmallIntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(8),
                ],
            ),
        ),
    ]
