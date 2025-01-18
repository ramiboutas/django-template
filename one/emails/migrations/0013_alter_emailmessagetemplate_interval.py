# Generated by Django 5.1.4 on 2025-01-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0012_rename_inverval_emailmessagetemplate_interval"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailmessagetemplate",
            name="interval",
            field=models.DurationField(blank=True, help_text="Min: 8:00:00", null=True),
        ),
    ]
