"""
Django settings for gartenkoop project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'


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

ALLOWED_HOSTS = ['gartenkoop.juntagrico.science', 'localhost', 'meine.gartenkooperative.li']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'gartenkoop',
    'juntagrico_stats',
    'juntagrico',
    'fontawesomefree',
    'import_export',
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
]

ROOT_URLCONF = 'gartenkoop.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','gartenkoop.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'gartenkoop.wsgi.application'


LANGUAGE_CODE = 'de'

USE_TZ = True
TIME_ZONE = 'Europe/Zurich'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
    
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     juntagrico Settings
"""
ORGANISATION_NAME = "Gartenkooperative"
ORGANISATION_LONG_NAME = "Gartenkooperative"
ORGANISATION_ADDRESS = {"name":"Gartenkooperative Region Liechtenstein-Werdenberg e.G.", 
            "street" : "Birkenweg",
            "number" : "6",
            "zip" : "9490",
            "city" : "Vaduz",
            "extra" : "Postfach 284"}
ORGANISATION_BANK_CONNECTION = {"PC" : "",
            "IBAN" : "LI13 0880 0548 1075 5200 1",
            "BIC" : "LILALI2XXXX",
            "NAME" : "",
            "ESR" : ""}
SHARE_PRICE = "250"

CONTACTS = {
    "general": "info@gartenkooperative.li"
}
ORGANISATION_WEBSITE = {
    'name': "meine.gartenkooperative.li",
    'url': "https://meine.gartenkooperative.li"
}
STYLES = {'static': ['gartenkoop/css/customize.css']}

BUSINESS_REGULATIONS = 'https://www.gartenkooperative.li/wp-content/uploads/171012_Betriebsreglement-der-Genossenschaft-Gartenkooperative-Region-Liechtenstein-Werdenberg.pdf'
BYLAWS = 'https://www.gartenkooperative.li/wp-content/uploads/2015/11/150226StatutenGartenkooperative.pdf'

MAIL_TEMPLATE = 'mails/email.html'

# needed?
FAQ_DOC = '/static/juntagrico/doc/fac.pdf'
EXTRA_SUB_INFO = '/static/juntagrico/doc/extra_sub_info.pdf'

SHARE_PRICE = '250'
CURRENCY = 'CHF'

ASSIGNMENT_UNIT = 'HOURS'

DEPOT_LIST_GENERATION_DAYS = [0, 1, 2, 3, 4, 5, 6]

BUSINESS_YEAR_START = {'day': 1, 'month': 1}
BUSINESS_YEAR_CANCELATION_MONTH = 10
MEMBERSHIP_END_MONTH = 12
MEMBERSHIP_END_NOTICE_PERIOD = 2

# Don't allow external signup
ENABLE_REGISTRATION = False

# USe a custom mailer that only sends to max 20 recipients at a time in the bcc, to or cc lists.
DEFAULT_MAILER = 'gartenkoop.gkmailer.Mailer'

# Send server emails from this address rather than root@localhost...
SERVER_EMAIL = 'info@gartenkooperative.li'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

ADMINS = (
    ('Gako Admin', os.environ.get('GAKO_ADMIN_EMAIL')),
)

IMAGES = {
    'status_100': '/static/juntagrico/img/status_100.png',
    'status_75': '/static/juntagrico/img/status_75.png',
    'status_50': '/static/juntagrico/img/status_50.png',
    'status_25': '/static/juntagrico/img/status_25.png',
    'status_0': '/static/juntagrico/img/status_0.png',
    'single_full': '/static/juntagrico/img/single_full.png',
    'single_empty': '/static/juntagrico/img/single_empty.png',
    'single_core': '/static/juntagrico/img/single_core.png',
    'core': '/static/juntagrico/img/core.png',
}

IMPERSONATE = {
    'ALLOW_SUPERUSER': True
}

# 1.4 settings

ADMINPORTAL_NAME = 'meine.gartekooperative'
ADMINPORTAL_SERVER_URL = 'meine.gartenkooperative.li'
STYLE_SHEET = '/static/gartenkoop/css/customize.css'

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'
