# Generated by Django 5.1.4 on 2025-01-19 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0017_rename_message_direction_messagesent_direction_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MessageSent",
            new_name="PostalMessage",
        ),
        migrations.AlterModelOptions(
            name="postalmessage",
            options={
                "base_manager_name": "prefetch_manager",
                "verbose_name": "Postal: Message",
                "verbose_name_plural": "Postal: Messages",
            },
        ),
    ]
