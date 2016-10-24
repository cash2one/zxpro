import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'h+sa6lbkb5ba#ym#s5x!2!c0zrg_bya5^v17(p70p9c=zh_o@u'
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'xhzx',
    'django_url_framework',
)

DATE_FORMAT = 'Y/m/d'
DATETIME_FORMAT = 'Y/m/d H:i:s'
TIME_FORMAT = 'H:i:'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'xhzxpro.urls'

WSGI_APPLICATION = 'xhzxpro.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'31.0.1.165',
        'NAME': 'newweb',
        'USER': 'root',
        'PASSWORD': 'midnet',
        'PORT': '5555',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'139.196.37.100',
        'NAME': 'newweb',
        'USER': 'root',
        'PASSWORD': 'midnet88',
        'PORT': '5555',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'127.0.0.1',
        'NAME': 'newweb',
        'USER': 'root',
        'PASSWORD': 'midnet88',
        'PORT': '5555',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'127.0.0.1',
        'NAME': 'newweb',
        'USER': 'root',
        'PASSWORD': 'midnet66',
        'PORT': '3306',
    }
}


LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
SESSION_COOKIE_AGE = 60 * 30
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'xadmin/templates/xadmin/'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'
CURYEAR = "2016"

