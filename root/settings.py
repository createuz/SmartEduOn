from pathlib import Path

from celery.schedules import crontab
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    # Front end
    "https://eduon.uz",
    "https://speaker.eduon.uz",
    "http://157.230.10.27:3001",
    # Islom front end
    "http://192.168.100.247:3000",
    "http://192.168.100.247:3001",
    "http://192.168.100.36:3000",
    "http://192.168.100.36:3001",
    "http://192.168.43.115:3000",
    "http://192.168.43.115:3001",
    "http://192.168.100.199:3000",
    "http://192.168.100.199:3001",
    # Ibrohim
    "http://192.168.10.203:3000",
    "http://192.168.10.203:3001",
    # ASKAR
    "http://192.168.1.40:8000",
    "http://192.168.1.40:5000"
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_URLS_REGEXES = [
    r'^/api1234/.*$',
    r'^/api-web/.*$',
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_PREFLIGHT_MAX_AGE = 86400

INSTALLED_APPS = [
    'adminlte3',
    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'backoffice.apps.BackofficeConfig',
    'rest_framework',
    'rest_framework_simplejwt',
    'paycomuz',
    'clickuz',
    'simplejwt',
    'paycom',
    'uniredpay',
    'corsheaders',
    'quiz',
    'rest_framework.authtoken',
    'django_filters',
    'background_task',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.users.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.users.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.users.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.users.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    "EXCEPTION_HANDLER": "root.utils.custom_exception_handler",

    'DEFAULT_PERMISSION_CLASSES': [
        'simplejwt.permissions.JwtPermission',
    ],

    'DEFAULT_FILTER_BACKENDS':
        [
            'django_filters.rest_framework.DjangoFilterBackend',
        ],

    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',

}

# click settings
# CLICK_SETTINGS = {
#     'service_id': '16632',
#     'merchant_id': '12015',
#     'secret_key': 'imOUAe56q2Zr8r',
#     'merchant_user_id': '17661'
# }

# PAYCOM_SETTINGS = {
#     "PAYCOM_API_KEY": "ZrTHJGJW05KjFX73IUWArAfyDDOscxO#e8MZ",
#     "PAYCOM_API_LOGIN": "Paycom",
#     "PAYCOM_ENV": False,  # test host
#     "TOKEN": "token",  # token
#     "SECRET_KEY": "password",  # password
#     "ACCOUNTS": {
#         "KEY_1": "order_id",
#         "KEY_2": None  # or "type"
#     }
# }

DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

# sms settings

SMS_EMAIL = 'ulugbekr2028@gmail.com'
SMS_SECRET_KEY = 'VUp0VI4q7Q3c7xffTgfSbVnbLZiStjP5nK4QHnNx'
SMS_BASE_URL = 'http://notify.eskiz.uz'
SMS_TOKEN = ''
SMS_TOKEN_GLOBAL = ''
SMS_CLIENT_ID = "R0lTd27bfzySEYrf"
SMS_SECRET_KEY_GLOBAL = 'QvvCvbrDMjYXbTMiV1VQ9jfODtVYFiiP'
SMS_BASE_URL_GLOBAL = 'https://auth.sms.to'
SMS_REGISTER_TEXT = 'Assalomu alaykum Eduon.uz saytimizga xush kelibsiz! Tasdiqlash kodi: '
SMS_ACCEPT_TEXT = 'Tabriklaymiz!!! Moderator tomonidan EduOn spiker akauntingiz faollashtirildi. https://speaker.eduon.uz/'
SMS_REJECT_TEXT = "Sizning profilingiz ma'lum sabablarga ko'ra aktivlashtirilmadi! https://speaker.eduon.uz/"

# unicoinc settings
UNICOIN_LOGIN = "eduon"
UNICOIN_PASSWORD = "SDqwd$se6l8Gp4ASMWmmhTxwO98Fiub9"
UNICOIN_HOST_UZCARD = "https://core.unired.uz/api/v1/unired"
UNICOIN_HOST_HUMO = "https://core.unired.uz/api/v1/humo"

UNIRED_LOGIN = "Eduon"
UNIRED_PASSWORD = "Nr9WAVeS1TjV"
UNIRED_WALLET_URL = "https://wallet.unired.uz"
UNIRED_ACCOUNT_BALANCE = ""

UZCARD_MERCHANT_ID = '90489428'
UZCARD_TERMINAL_ID = '92415924'

HUMO_MERCHANT_ID = '011860000118613'
HUMO_TERMINAL_ID = '23610C9U'

# email settings
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# celery settings
CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE')
CELERY_TASK_TRACK_STARTED = os.getenv('CELERY_TASK_TRACK_STARTED')
CELERY_TASK_TIME_LIMIT = os.getenv('CELERY_TASK_TIME_LIMIT')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_BEAT_SCHEDULER = os.getenv('CELERY_BEAT_SCHEDULER')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULE = {
    "set_discount_to_random_courses": {
        "task": "set_discount_to_random_courses",
        "schedule": crontab(hour=13, day_of_week=0)
    },
    "delete_discount_task": {
        "task": "delete_discount_task",
        "schedule": crontab()
    },
    "print_test": {
        "task": "print_test",
        "schedule": crontab()
    }
}
