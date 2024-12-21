# Generated by Django 5.1.4 on 2024-12-21 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_rename_folder_article_folder_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "base_manager_name": "prefetch_manager",
                "ordering": ["folder_name", "-created_on"],
            },
        ),
        migrations.RenameField(
            model_name="article",
            old_name="can_be_shown_in_home",
            new_name="featured",
        ),
    ]
