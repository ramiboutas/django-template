# Generated by Django 5.1.3 on 2024-11-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_hero_headline_de_hero_headline_en_hero_headline_es_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="hero",
            name="allow_field_translation",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="homepage",
            name="allow_field_translation",
            field=models.BooleanField(default=False),
        ),
    ]
