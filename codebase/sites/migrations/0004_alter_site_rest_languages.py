# Generated by Django 5.1.4 on 2024-12-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_initial"),
        ("sites", "0003_alter_site_article_folders_alter_site_books_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="rest_languages",
            field=models.ManyToManyField(
                blank=True,
                related_name="sites_with_rest_languages",
                to="base.language",
                verbose_name="Rest of languages",
            ),
        ),
    ]
