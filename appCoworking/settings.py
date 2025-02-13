from pathlib import Path
from decouple import config
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n!#91^8#haw^dkjfi+dz&$u35=yffrd^4%wcz_heq32#u2(u^5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["app-coworking.onrender.com"]

CSRF_TRUSTED_ORIGINS = ["https://app-coworking.onrender.com"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_tailwind",
    "coworking",
    "review",
    "reservation",
    "users",
    "landingPages",
    "payments",
    "assistant",
    "rest_framework",
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

ROOT_URLCONF = "appCoworking.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "appCoworking.context_processors.user_profile",  # Añadir aquí
            ],
        },
    },
]

WSGI_APPLICATION = "appCoworking.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT", cast=int),
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

LANGUAGE_CODE = "es-EC"

TIME_ZONE = "America/Guayaquil"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

LOGIN_REDIRECT_URL = "coworking_list"
LOGOUT_REDIRECT_URL = "login"


WHATSAPP_API_URL = "https://graph.facebook.com/v21.0"
WHATSAPP_PHONE_NUMBER_ID = "202550156272879"
WHATSAPP_ACCESS_TOKEN = "EAAeHpj06JZCEBO0xId3Wh0IRZCjWDoM6irhPTMCnHZCS5fZBZCQ3d6abDp6mAaUB4UPPwZAwkOLFai7eGMg6rnRPHxlZCD2iAVc7WnT7IIquenmkveX0wrgY9ur6fZC130PF85GaMhPTEB80FtGBxdmDPn2WSNkAdnX04IC1ZBFZCK4A6KU0JXnMVeI4C0krdPw6NiSHUQEl2aPUiKMWrVLo8XJw1R82wV"

TWILIO_ACCOUNT_SID = "ACfe2a2a42e62d03e698aa4c60d648cdaf"
TWILIO_AUTH_TOKEN = "efa20e046733eb6480e07d940ffac96a"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Número de WhatsApp de Twilio

OPENAI_API_KEY = config("OPENAI_API_KEY")


# settings.py
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "electrosonix12@gmail.com"
EMAIL_HOST_PASSWORD = "jssx kiwl tymm nuwl"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "electrosonix12@gmail.com"
