# Generated by Django 5.1.4 on 2025-01-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0018_rename_messagesent_postalmessage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="postalmessage",
            name="delayed",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="postalmessage",
            name="delivery_failed",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="postalmessage",
            name="held",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
