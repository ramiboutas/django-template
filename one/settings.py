"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# 0. Setup
from copy import copy
from datetime import datetime
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from environs import Env
from redis import ConnectionPool as RedisConnectionPool

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()
now = datetime.now()


SECRET_KEY = env("SECRET_KEY", "some-tests-need-a-secret-key")
ENV = env("ENV")
DEBUG = env.bool("DEBUG")
HTTPS = env.bool("HTTPS")
STATIC_HOST = env("STATIC_HOST", "")

REDIS_URL = env("REDIS_URL")
REDIS_CONNECTION_POOL = RedisConnectionPool.from_url(url=REDIS_URL)


"""
##################
1. Django settings
##################
"""

ALLOWED_HOSTS = [
    "127.0.0.1",
    # personal site
    "ramib.ch",
    "www.ramib.ch",
    # dgt tests
    "dgt-tests.ramib.ch",
    "dgttests.es",
    "www.dgttests.es",
    # personal site 2 (will be removed)
    "ramiboutas.com",
    "www.ramiboutas.com",
    # english quizzes
    "englishstuff.online",
    "www.englishstuff.online",
    # nice cv
    "nicecv.online",
    "www.nicecv.online",
]


INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS = [
    # Apps that need to be on top
    "daphne",
    # Third-party apps
    "django_cleanup.apps.CleanupConfig",
    "django_extensions",
    "markdownify.apps.MarkdownifyConfig",
    "modeltranslation",
    "huey.contrib.djhuey",
    "rosetta",
    "allauth",
    "allauth.account",
    "geoip2",
    "djmoney",
    "channels",
    "dbbackup",
    "corsheaders",
    "debug_toolbar",
    "django_browser_reload",
    "django_minify_html",
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.db.migrations",
    "django.contrib.admindocs",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.linkedin_oauth2",
    # Project apps
    "one.base",
    "one.clients",
    "one.articles",
    "one.pages",
    "one.menus",
    "one.search",
    "one.tex",
    "one.users",
    "one.home",
    "one.plans",
    "one.tools",
    "one.links",
    "one.faqs",
    "one.sites",
    "one.products",
    "one.books",
    "one.chat",
    "one.geo",
    "one.quiz",
    "one.dgt",
]

MIDDLEWARE = [
    "one.base.middleware.ip.IpAddressMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "one.base.middleware.one.OneMiddleware",
    "django_minify_html.middleware.MinifyHtmlMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "one.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "one" / "_templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "one.base.utils.context_processors.site_utilities",
            ],
            "debug": DEBUG,
        },
    },
    {
        "NAME": "tex",
        "BACKEND": "one.tex.backend.TeXEngine",
        "DIRS": [BASE_DIR / "one" / "_tex_templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "one.tex.environment.environment",
        },
    },
]

WSGI_APPLICATION = "one.wsgi.application"

ASGI_APPLICATION = "one.asgi.application"

# Database
DB_SUPERUSER = env("POSTGRES_SUPERUSER")
DB_SUPERPASSWORD = env("POSTGRES_SUPERPASSWORD")
DB_NAME = env("POSTGRES_DB")
DB_USER = env("POSTGRES_USER")
DB_PASSWORD = env("POSTGRES_PASSWORD")
DB_HOST = env("POSTGRES_HOST")
DB_PORT = env("POSTGRES_PORT")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "TEST": {"NAME": "test_db"},
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa: E501
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

# Authentication
AUTH_USER_MODEL = "users.User"

# Internationalization
LANGUAGE_CODE = "en"  # default language

TIME_ZONE = "Europe/Zurich"

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ("de", _("German")),
    ("es", _("Spanish")),
    ("fr", _("French")),
    ("el", _("Greek")),
    ("it", _("Italian")),
    ("nl", _("Dutch")),
    ("pl", _("Polish")),
    ("pt", _("Portuguese")),
    ("ru", _("Russian")),
    ("sk", _("Slovak")),
    ("sl", _("Slovenian")),
    ("sv", _("Swedish")),
    ("tr", _("Turkish")),
    ("uk", _("Ukrainian")),
]

LANGUAGE_CODES = [items[0] for items in LANGUAGES]
LANGUAGE_CODES_WITHOUT_DEFAULT = copy(LANGUAGE_CODES)
LANGUAGE_CODES_WITHOUT_DEFAULT.remove(LANGUAGE_CODE)

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# A list of trusted origins for unsafe requests (e.g. POST).
# https://docs.djangoproject.com/en/5.1/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = [
    # TODO: Add here h
]


# Superuser without input

DJANGO_SUPERUSER_USERNAME = env("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_PASSWORD = env("DJANGO_SUPERUSER_PASSWORD")
DJANGO_SUPERUSER_EMAIL = env("DJANGO_SUPERUSER_EMAIL")

# Caching
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_URL,
    }
}


"""
####################
Third-party settings
####################
"""

# huey


HUEY = {
    "huey_class": "huey.RedisHuey",  # Huey implementation to use.
    "name": DATABASES["default"]["NAME"],  # Use db name for huey.
    "results": True,  # Store return values of tasks.
    "store_none": False,  # If a task returns None, do not save to results.
    "immediate": ENV == "dev",  # If DEBUG=True, run synchronously.
    "utc": True,  # Use UTC for all times internally.
    "blocking": True,  # Perform blocking pop rather than poll Redis.
    "connection": {"connection_pool": REDIS_CONNECTION_POOL},
    "consumer": {
        "workers": 2,
        "worker_type": "thread",
        "initial_delay": 0.1,  # Smallest polling interval, same as -d.
        "backoff": 1.15,  # Exponential backoff using this rate, -b.
        "max_delay": 10.0,  # Max possible polling interval, -m.
        "scheduler_interval": 1,  # Check schedule every second, -s.
        "periodic": True,  # Enable crontab feature.
        "check_worker_health": True,  # Enable worker health checks.
        "health_check_interval": 1,  # Check worker health every second.
    },
}

# cors

CORS_ALLOWED_ORIGINS = []


# geoip2

GEOIP_PATH = BASE_DIR / "geoip2dbs"


# django-markdownify
# https://django-markdownify.readthedocs.io/en/latest/settings.html


MARKDOWNIFY = {
    "default": {
        "WHITELIST_ATTRS": ["href", "src", "alt", "class"],
        "WHITELIST_TAGS": [
            "a",
            "abbr",
            "acronym",
            "b",
            "blockquote",
            "em",
            "i",
            "li",
            "ol",
            "p",
            "strong",
            "ul",
            "img",
            "span",
            "div",
            "pre",
            "code",
        ],
        "MARKDOWN_EXTENSIONS": [
            "markdown.extensions.codehilite",
            "markdown.extensions.extra",
            "markdown.extensions.footnotes",
            "markdown.extensions.tables",
        ],
        "MARKDOWN_EXTENSION_CONFIGS": {
            "markdown.extensions.codehilite": {
                "css_class": "codehilite",
                "linenums": False,
            },
        },
    }
}

# Email and django-o365
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = "django_o365mail.EmailBackend"
O365_MAIL_CLIENT_ID = env("O365_MAIL_CLIENT_ID")
O365_MAIL_CLIENT_SECRET = env("O365_MAIL_CLIENT_SECRET")
O365_MAIL_TENANT_ID = env("O365_MAIL_TENANT_ID")
O365_MAIL_MAILBOX_KWARGS = {"resource": EMAIL_HOST_USER}
O365_MAIL_SAVE_TO_SENT = True


## Translations

# DeepL
DEEPL_AUTH_KEY = env("DEEPL_AUTH_KEY")


# Rosetta
# https://django-rosetta.readthedocs.io/settings.html
ROSETTA_MESSAGES_PER_PAGE = 50
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_WSGI_AUTO_RELOAD = True

# modeltranslation
MODELTRANSLATION_DEBUG = DEBUG

# django-allauth

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


ACCOUNT_LOGOUT_REDIRECT = "/"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_URL = "account_login"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


SOCIALACCOUNT_PROVIDERS = {
    # https://django-allauth.readthedocs.io/en/latest/providers.html#google
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": env("SOCIALACCOUNT_GOOGLE_CLIENT_ID"),
            "secret": env("SOCIALACCOUNT_GOOGLE_SECRET_KEY"),
            "key": "",
        }
    },
    "linkedin_oauth2": {
        "APP": {
            "client_id": env("SOCIALACCOUNT_LINKEDIN_CLIENT_ID"),
            "secret": env("SOCIALACCOUNT_LINKEDIN_SECRET_KEY"),
            "key": "",
        },
        "SCOPE": ["r_liteprofile", "r_emailaddress", "w_member_social"],
        "PROFILE_FIELDS": [
            "id",
            "first-name",
            "last-name",
            "email-address",
            "picture-url",
            "public-profile-url",
            "openid",
        ],
    },
}


# channels


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}


# Stripe

STRIPE_PUBLIC_KEY = env("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET")

# Linkedin posts
# TODO: change this! Use Site model to store these keys.
LINKEDIN_AUTHOR_TPYE = "organization"  # "organization" or "person"
LINKEDIN_AUTHOR_ID = ""
LINKEDIN_ACCESS_TOKEN = ""
LINKEDIN_REFRESH_TOKEN = ""


"""
################
Project settings
################
"""

CLEAR_CACHE_IN_DEV = True


# Tex
# TODO: check if it is posible to pass an arg. to run tex without this setting.
LATEX_GRAPHICSPATH = []


# Submodules
SUBMODULES_PATH = BASE_DIR / "submodules"


# Telegram
# 1. Use BotFather to get API KEY: https://telegram.me/BotFather
# 2. (Admin): Write something to Bot in Telegram
# 3. Read the updates: one.base.utils.telegram.Bot.get_updates

TELEGRAM_BOT_API_KEY = env("TELEGRAM_BOT_API_KEY")
TELEGRAM_ADMIN_CHAT_ID = env("TELEGRAM_ADMIN_CHAT_ID", "1777934566")


# Whatsapp
# https://developers.facebook.com/docs/whatsapp/cloud-api/messages/text-messages
WHATSAPP_API_ACCESS_TOKEN = env("WHATSAPP_API_ACCESS_TOKEN")
WHATSAPP_BUSINESS_PHONE_NUMBER_ID = env("WHATSAPP_BUSINESS_PHONE_NUMBER_ID")


# Media and static files (S3)
AWS_S3_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")

S3_BASE_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/"
MEDIA_URL = S3_BASE_URL + "media/"
STATIC_URL = S3_BASE_URL + "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = STATIC_HOST + "/static/"

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "gzip": False,
            "default_acl": "public-read",
            "location": "media",
            "querystring_auth": False,
        },
    },
    "private": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "gzip": False,
            "default_acl": "private",
            "location": "private",
            "querystring_auth": True,
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    # "staticfiles": {
    #     "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    #     "OPTIONS": {
    #         "gzip": True,
    #         "default_acl": "public-read",
    #         "querystring_auth": False,
    #     },
    # },
}

# DB backups
# https://django-dbbackup.readthedocs.io/en/stable/storage.html#amazon-s3
DBBACKUP_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DBBACKUP_STORAGE_OPTIONS = {
    "access_key": AWS_S3_ACCESS_KEY_ID,
    "secret_key": AWS_S3_SECRET_ACCESS_KEY,
    "bucket_name": AWS_STORAGE_BUCKET_NAME,
    "location": f"db_backups/{now.year}/{now.month}/",
    "default_acl": "private",
}


if HTTPS:
    # https in production
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31_536_000  # 31536000 # usual: 31536000 (1 year)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
