# Generated by Django 5.1.3 on 2024-11-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "base",
            "0004_rename_translate_fields_from_default_language_extendedsite_translate_fields_from_default",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="extendedsite",
            old_name="translate_fields_from_default",
            new_name="allow_field_translation",
        ),
    ]
