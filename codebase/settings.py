"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

## 0. Setup
import os
from datetime import datetime
from pathlib import Path

import dotenv
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file

dotenv.load_dotenv(dotenv_path=BASE_DIR / ".env")


HTTPS = os.environ.get("HTTPS", "") == "1"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "some-tests-need-a-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "") == "1"


## 1. Django settings


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.db.migrations",
    # Third-party apps
    "django_cleanup.apps.CleanupConfig",
    "django_extensions",
    "markdownx",
    "modeltranslation",
    "huey.contrib.djhuey",
    "rosetta",
    # Project apps
    "codebase.base",
    "codebase.articles",
    "codebase.pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "codebase.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "codebase.base.context_processors.menus_and_links",
            ],
        },
    },
]

WSGI_APPLICATION = "codebase.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en"  # default language

TIME_ZONE = "Europe/Zurich"

USE_I18N = True

USE_TZ = True

LANGUAGES = [("en", _("English")), ("de", _("German")), ("es", _("Spanish"))]

LANGUAGE_CODES = ["en", "de", "es"]

LANGUAGE_CODES_WITHOUT_DEFAULT = ["de", "es"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


## Third-party settings
# django-markdownx & python-markdown
# https://pypi.org/project/django-markdownx/
# https://neutronx.github.io/django-markdownx/customization/
MARKDOWNX_MEDIA_PATH = datetime.now().strftime("markdownx/%Y/%m/%d")
MARKDOWNX_IMAGE_MAX_SIZE = {"size": (1920, 0), "quality": 100}
# https://python-markdown.github.io/extensions/
MARKDOWN_EXTENSION_CONFIGS = {
    "markdown.extensions.codehilite": {
        "css_class": "codehilite",
        "linenums": False,
        "guess_lang": False,
    }
}
MARKDOWN_EXTENSIONS = [
    "markdown.extensions.codehilite",
    "markdown.extensions.fenced_code",
    "markdown.extensions.footnotes",
    "markdown.extensions.tables",
]

# django-o365 and Email
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = "django_o365mail.EmailBackend"
O365_MAIL_CLIENT_ID = os.environ.get("O365_MAIL_CLIENT_ID")
O365_MAIL_CLIENT_SECRET = os.environ.get("O365_MAIL_CLIENT_SECRET")
O365_MAIL_TENANT_ID = os.environ.get("O365_MAIL_TENANT_ID")
O365_MAIL_MAILBOX_KWARGS = {"resource": EMAIL_HOST_USER}
O365_MAIL_SAVE_TO_SENT = True


## Project settings

# Website

WEBSITE_NAME = "Example site"
WEBSITE_URL = "http://127.0.0.1/"

# telegram

TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
TELEGRAM_ADMIN_CHAT_ID = os.environ.get("TELEGRAM_ADMIN_CHAT_ID")


# submodules

# article topics
ARTICLES_MARKDOWN_PATH = BASE_DIR / "submodules" / "articles"
SYNC_ARTICLE_TOPICS = ("example-topic",)

# pages
PAGES_MARKDOWN_PATH = BASE_DIR / "submodules" / "pages"
SYNC_PAGE_TOPICS = ("general-pages",)

# https

if HTTPS:  # pragma: no cover
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31_536_000  # 31536000 # usual: 31536000 (1 year)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
