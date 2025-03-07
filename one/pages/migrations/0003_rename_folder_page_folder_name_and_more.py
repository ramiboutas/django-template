# Generated by Django 5.1.4 on 2024-12-19 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="page",
            old_name="folder",
            new_name="folder_name",
        ),
        migrations.RenameField(
            model_name="page",
            old_name="subfolder",
            new_name="subfolder_name",
        ),
        migrations.AlterUniqueTogether(
            name="page",
            unique_together={("folder_name", "subfolder_name")},
        ),
    ]
