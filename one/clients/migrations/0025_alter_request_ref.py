# Generated by Django 5.1.4 on 2025-03-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0024_alter_pathredirect_applicable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="ref",
            field=models.CharField(db_index=True, max_length=512, null=True),
        ),
    ]
