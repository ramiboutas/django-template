from django.apps import AppConfig


class FaqsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "codebase.faqs"

    def ready(self):  # pragma: no cover
        from . import signals  # noqa
