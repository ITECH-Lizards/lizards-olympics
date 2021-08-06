"""
Django settings for hengDaProject project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^je$#q_n6alr1wt$uhe$zb2=77r86kt&4hpi%we&1l!3y7lw#='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homeApp',          # 添加"首页"应用
    'aboutApp',         # 添加"公司简介"应用
    'contactApp',       # 添加"人才招聘"应用
    'newsApp',          # 添加"新闻动态"应用
    'DjangoUeditor',    # 添加富文本应用
    'haystack',         # 添加搜索应用
    'widget_tweaks',    # 添加模型表单组件定制化渲染应用
    'comment',
    'users',
    'sorl.thumbnail',   #缩略图
    'social_django', # 新增GitHub登录
    #'registration',     # 认证模块
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hengDaProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', # 新增
                'social_django.context_processors.login_redirect', #新增
            ],
        },
    },
]

WSGI_APPLICATION = 'hengDaProject.wsgi.application'
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
) # 新增

SOCIAL_AUTH_URL_NAMESPACE = 'social' # 新增


SOCIAL_AUTH_GITHUB_KEY = '633185bcecfd2e2241bc'
SOCIAL_AUTH_GITHUB_SECRET = '3fefc0308fbde9fb392b2e63b3acea905556f851'
SOCIAL_AUTH_GITHUB_USE_OPENID_AS_USERNAME = True

# 登陆成功后的回调路由
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/' # 登陆成功之后的路由
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'   # 设置语言为中文
TIME_ZONE = 'Asia/Shanghai' # 设置中国时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# 新闻搜索配置django-haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'newsApp.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE  =  10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# 邮箱设置
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxxxxxxx@qq.com'      # QQ 账号
EMAIL_HOST_PASSWORD = 'xxxxxxxx'         # 授权码
EMAIL_USE_TLS = True

#配置缓存表
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table_home',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 2000
        }
    }
}

REGISTRATION_OPEN = True
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = 'homeApp:lizards'
LOGIN_URL = 'auth_login'
AUTH_USER_MODEL = 'users.User'