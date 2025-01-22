# Generated by Django 5.1.4 on 2025-01-22 06:25

import one.emails.models
import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0021_postalreplymessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="postalreplymessage",
            name="draft",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="postalreplymessage",
            name="file",
            field=models.FileField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(
                    default_acl="private",
                    gzip=False,
                    location="private",
                    querystring_auth=True,
                ),
                upload_to=one.emails.models.PostalReplyMessage.get_directory,
            ),
        ),
    ]
