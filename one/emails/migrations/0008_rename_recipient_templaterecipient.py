# Generated by Django 5.1.4 on 2025-01-17 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0007_sender_alter_domaindnserror_options_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Recipient",
            new_name="TemplateRecipient",
        ),
    ]
