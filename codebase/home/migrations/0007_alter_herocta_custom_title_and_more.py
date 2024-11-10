# Generated by Django 5.1.3 on 2024-11-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_homepage_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="herocta",
            name="custom_title",
            field=models.CharField(default="Rename me", max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="herocta",
            name="custom_title_de",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="herocta",
            name="custom_title_en",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="herocta",
            name="custom_title_es",
            field=models.CharField(max_length=128, null=True),
        ),
    ]
