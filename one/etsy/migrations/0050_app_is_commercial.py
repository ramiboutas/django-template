# Generated by Django 5.1.4 on 2025-02-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("etsy", "0049_alter_etsyauth_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="is_commercial",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
