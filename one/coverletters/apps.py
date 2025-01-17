from django.apps import AppConfig


class CoverlettersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "one.coverletters"

    def ready(self):  # pragma: no cover
        from . import signals  # noqa
