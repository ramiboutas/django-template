# Generated by Django 5.1.4 on 2024-12-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0006_alter_client_geoinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="geoinfo",
            name="city",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="geoinfo",
            name="continent_name",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="geoinfo",
            name="latitude",
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="geoinfo",
            name="longitude",
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="geoinfo",
            name="region_name",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="geoinfo",
            name="time_zone",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="geoinfo",
            unique_together={("latitude", "longitude")},
        ),
    ]
