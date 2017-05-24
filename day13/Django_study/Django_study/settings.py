# -*- coding:utf-8 -*-
"""
Django settings for Django_study project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5)z34%$l!eu%+2&!fbu2oo9&@5i=csd6fd8*jy62a_ry_4i41+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
#指定一下我们的模板文件的存放路径   注意那个,必须有的
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'template'),    
    )
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #'oldboy.mymiddleware.Day13Middleware',
    #导入自定义的中间件
)

ROOT_URLCONF = 'Django_study.urls'

WSGI_APPLICATION = 'Django_study.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#连接mysql驱动配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Django_study',
        'USER':'zhangyage',
        'PASSWORD':'zhangyage',
        'HOST':'192.168.75.133',
        'PORT':'3306',
    }
} 

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#配置静态文件存放的路径
STATIC_URL = '/static/'
STATICFILES_DIRS = (
        os.path.join(BASE_DIR,'static'),
    )


#SESSION_COOKIE_AGE = 10
#设置session的过期时间  10S