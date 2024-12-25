# Generated by Django 5.1.4 on 2024-12-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0008_alter_client_geoinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="ip_address",
            field=models.GenericIPAddressField(db_index=True, unique=True),
        ),
    ]
