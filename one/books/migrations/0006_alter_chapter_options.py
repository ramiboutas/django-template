# Generated by Django 5.1.4 on 2024-12-21 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_alter_book_pdf"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chapter",
            options={
                "base_manager_name": "prefetch_manager",
                "ordering": ["folder_name", "-created_on"],
            },
        ),
    ]
