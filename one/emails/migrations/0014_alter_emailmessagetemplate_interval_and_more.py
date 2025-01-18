# Generated by Django 5.1.4 on 2025-01-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0013_alter_emailmessagetemplate_interval"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailmessagetemplate",
            name="interval",
            field=models.DurationField(
                blank=True,
                help_text="Set when email message is periodic. Min: 8:00:00",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="emailmessagetemplate",
            name="is_periodic",
            field=models.BooleanField(
                default=False, help_text="Email message will be send periodically."
            ),
        ),
        migrations.AlterField(
            model_name="emailmessagetemplate",
            name="start_time",
            field=models.DateField(
                blank=True, help_text="Set when email message is periodic.", null=True
            ),
        ),
        migrations.AlterField(
            model_name="emailmessagetemplate",
            name="stop_time",
            field=models.DateField(
                blank=True, help_text="Set when email message is periodic.", null=True
            ),
        ),
    ]
