from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "one.jobs"

    def ready(self):  # pragma: no cover
        from . import signals  # noqa
