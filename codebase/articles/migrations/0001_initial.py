# Generated by Django 5.1.3 on 2024-11-16 18:07

import auto_prefetch
import codebase.utils.abstracts
import codebase.utils.mixins
import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticlesFolder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                ("is_premium", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(editable=False, max_length=256)),
                (
                    "title_en",
                    models.CharField(editable=False, max_length=256, null=True),
                ),
                (
                    "title_de",
                    models.CharField(editable=False, max_length=256, null=True),
                ),
                (
                    "title_es",
                    models.CharField(editable=False, max_length=256, null=True),
                ),
                ("slug", models.SlugField(editable=False, max_length=128, unique=True)),
                (
                    "slug_en",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                (
                    "slug_de",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                (
                    "slug_es",
                    models.SlugField(
                        editable=False, max_length=128, null=True, unique=True
                    ),
                ),
                ("folder", models.CharField(editable=False, max_length=128)),
                ("subfolder", models.CharField(editable=False, max_length=256)),
                ("body", models.TextField(editable=False)),
                ("body_en", models.TextField(editable=False, null=True)),
                ("body_de", models.TextField(editable=False, null=True)),
                ("body_es", models.TextField(editable=False, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "featured",
                    models.BooleanField(
                        default=False,
                        help_text="If featured it will be showed in home ",
                        verbose_name="Featured article",
                    ),
                ),
                ("allow_comments", models.BooleanField(default=True)),
                ("sites", models.ManyToManyField(to="sites.site")),
                (
                    "submodule_folder",
                    auto_prefetch.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="articles.articlesfolder",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            bases=(models.Model, codebase.utils.mixins.PageMixin),
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ArticleFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "file",
                    models.FileField(
                        upload_to=codebase.utils.abstracts.upload_page_file
                    ),
                ),
                (
                    "parent_page",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(max_length=512, verbose_name="Comment")),
                (
                    "article",
                    auto_prefetch.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articles.article",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "prefetch_manager",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("prefetch_manager", django.db.models.manager.Manager()),
            ],
        ),
    ]
