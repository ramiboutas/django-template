# Generated by Django 5.1.4 on 2024-12-22 13:07

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_alter_chapter_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="pdf",
            field=models.FileField(
                null=True,
                storage=storages.backends.s3.S3Storage(
                    default_acl="private",
                    gzip=False,
                    location="private",
                    querystring_auth=True,
                ),
                upload_to="books/",
            ),
        ),
    ]
