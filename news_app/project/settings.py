import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# модуль Д11.2
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ih%n$n4g-&dyjs0nlo1u^+=6^@q!mtqmka8hy8r+r1lmpb6f5t'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# Модуль Д5
ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # приложения для модуля Д1-3
    'django.contrib.sites',
    'django.contrib.flatpages',

    # приложения для модуля Д4 (фильтры по словам)
    'newapp',
    'django_filters',  # чтоб фильтра поддерживались

    # приложения для модуля Д5 (регистрация, аутентификация пользователей)
    'sign',
    'protect',

    # чтоб возможно было авторизоваться через сторонние сервисы, такие как гугл
    # пакет pip install django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # приложения для модуля Д6 (подписчики и рассылка писем по расписанию)
    # надо указать не имя нашего приложения, а его конфиг, чтобы всё заработало
    'appointments.apps.AppointmentConfig',
    'django_apscheduler',

]

DEFAULT_FROM_EMAIL = 'factoryskill@yandex.ru'

# используется в случае, если данный проект управляет несколькими сайтами
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'

]

ROOT_URLCONF = 'project.urls'

# это все, что относится по части шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # путь, где лежат нами созданные шаблоны по умолчанию
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Прошлая база данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Модуль Д12 - база данных postgreSQL (пустая, поэтому отключена)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# чтобы админ панель отображалась на русском языке
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'  # для перевода на русский

# часовой пояс (задано время - самара)
TIME_ZONE = 'Europe/Samara'
# TIME_ZONE = 'UTC'

USE_I18N = True

# USE_L10N = True

# USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# модуль Д14
LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'English'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "newapp/static"
]

# для модуля Д5 (прошлая версия ссылки)

# Django перенаправляет неавторизованных пользователей на страницу входа, указанного по данному пути
# LOGIN_URL = 'sign/login/'

# Чтобы возможно было авторизоваться через сторонние сервисы, такие как гугл, создаем другую форму и
# указываем другой адрес
LOGIN_URL = '/accounts/login/'

# При корректных данных для входа, пользователь перенаправляется на страницу, указанною по данному пути
# страница, куда перенаправляется пользователь после успешного входа на сайт
LOGIN_REDIRECT_URL = '/news/'

# модуль Д5, чтоб можно было авторизоваться через сторонние сервисы, нужно «включить»
# аутентификацию как по username, так и специфичную по email или сервис-провайдеру
AUTHENTICATION_BACKENDS = [

    # добавить бэкенды аутентификации: встроенный бэкенд Django, реализующий аутентификацию по username
    'django.contrib.auth.backends.ModelBackend',

    # бэкенд аутентификации, предоставленный пакетом allauth
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Первые два указывают на то, что поле email является обязательным и уникальным, а третий, наоборот, говорит,
# что username теперь необязательный. Следующий параметр указывает, что аутентификация будет происходить
# посредством электронной почты. Напоследок мы указываем, что верификация почты отсутствует. Обычно на почту
# отправляется подтверждение аккаунта, после подтверждения которого восстанавливается полная функциональность
# учетной записи. Для тестового примера нам не обязательно это делать.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

# Модуль Д6 - настройка отправки почты
EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же всегда
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый всегда
EMAIL_HOST_USER = 'factoryskill'  # имя пользователя, например, если почта user@yandex.ru, то надо
# писать user, иными словами, это всё то что идёт до собачки (@)
EMAIL_HOST_PASSWORD = 'qazwsx963852'  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, включать обязательно, защита от хакеров

# список всех админов в формате ('имя', 'их почта')
# если хотим отправлять письма только админам (статут пользователя = все права)
ADMINS = [
    ('Mail', 'ges1987@list.ru'),
    ('Yandex', 'ges300487@yandex.ru')
]

MANAGERS = [
    ('Mail', 'ges1987@list.ru'),
    ('Yandex', 'ges300487@yandex.ru')
]

SERVER_EMAIL = 'factoryskill@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

# Модуль 6.3 - подтверждение регистрации через почту
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTIFICTION_METHOD = 'email'

# Модуль 6.5 - действия по расписанию
# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше,
# но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

# Модуль Д7 - Celery,Redis
# указывает на URL брокера сообщений (Redis). По умолчанию он находится на порту 6379
# чтоб настроить правильную работу для винды среды
# заменяем это (см ниже)
# CELERY_BROKER_URL = 'redis://localhost:6379'
# по такому правилу
# redis://:password@hostname:port/db_number
# db_number = 0, обязательно, иначе ошибки будут
# на это
CELERY_BROKER_URL = 'redis://:SLltAfLjaeIah58aXZBP6rICl6g60J2N@redis-16974.c258.us-east-1-4.ec2.cloud.redislabs.com:16974/0'

# куда будут отправляться все данные, указывает на хранилище результатов выполнения задач
# заменяем это
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# на это
CELERY_RESULT_BACKEND = 'redis://:SLltAfLjaeIah58aXZBP6rICl6g60J2N@redis-16974.c258.us-east-1-4.ec2.cloud.redislabs.com:16974/0'
# формат наших данных
CELERY_ACCEPT_CONTENT = ['application/json']
# формат данных, метод сериализации задач
CELERY_TASK_SERIALIZER = 'json'
# формат данных, метод сериализации результатов
CELERY_RESULT_SERIALIZER = 'json'

# Модуль Д8 - кэширование страничек сайта
CACHES = {
    'default': {
        'TIMEOUT': 30,  # добавляем стандартное время ожидания в минуту (по умолчанию это 5 минут — 300 секунд)
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),  # BASE_DIR - значит папка проекта Указываем, куда
        # будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

#
# Модуль Д13 - логирование
# 1 - (без изменений) просто единица
# 2 - без изменений (контролирует работу существующей схемы логирования Django)
# 3 - варианты (форматы) вывода информации (сообщений)
# 4 - для уровня дебага делаем вывод инфы
# (asctime) - время возникновения сообщения
# (levelname) - уровень логирования
# (module) - модуль-источник сообщения
# (message) - само сообщени
# (process) - процесс
# (thread) - поток, в которых оно возникло сообщений
# (pathname) - путь к источнику события
# (exc_info) - стэк ошибки
# 5 - фильтр, который пропускает сообщения в зависимости от состояния переменной DEBUG, например, если она
# (DEBUG = True), то выводить сообщения и т.д.
# 6 - хендлер, то есть обработчик, когда мы получили сообщение, обработчик может вывести его в
# соответствии с форматом, фильтрами, уровнями либо в консоль, либо записать в файл, либо отправить по почте
LOGGING = {
    'version': 1,  # 1
    'disable_existing_loggers': False,  # 2
    'formatters': {  # 3

        # 1-3 пункт задания
        # для уровня DEBUG - время, уровень логирования, сообщение
        'debug_console': {  # 4
            # 'format': '{asctime} :: {levelname} -- {message}',
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s',
        },
        # для уровня WARNING - время, уровень логирования, путь к событию, сообщение
        'warning_console': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        },

        # 3 пункт задания
        # для уровней ERROR и CRITICAL - время, уровень логирования, путь к событию, сообщение, стэк ошибки
        # для файла errors.log
        'error_critical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },

        # 2-4 пункт задания - время, уровень логирования, модуль, сообщение
        # для файлов general.log и security.log
        'general_security_log': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },

        # 5 пункт задания - время, уровень логирования, путь к событию, сообщение
        # для уровня ERROR, для отправки по почте
        'mail_log': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        }
    },

    'filters': {  # 5
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {  # 6

        # 1 пункт задания - уровень DEBUG, фильтр DEBUG = True везде, кроме отправки по почте и
        # записи в файл general.log
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug_console'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_console'
        },

        # 2 пункт задания, уровень INFO, фильтр DEBUG = False
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general_security_log'
        },

        # 4 пункт задания, уровень INFO
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general_security_log'
        },

        # 3 пункт задания - уровень ERROR, вывод в файл errors.log
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },

        # 3 пункт задания - уровень CRITICAL, вывод в файл errors.log
        'file_critical': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_critical'
        },

        # 5 пункт задания - уровень ERROR, отправка по почте
        'mail_admin': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail_log'
        }
    },

    'loggers': {  # 6 формируем логеров

        # 1, 2 пункт задания
        'django': {
            'handlers': ['console_debug', 'console_warning', 'file_general'],
            'propagate': True,
        },

        # 3 пункт задания
        'django.template': {
            'handlers': ['file_errors', 'file_critical'],
            'propagate': True,
        },

        # 3 пункт задания
        'django.db_backends': {
            'handlers': ['file_errors', 'file_critical'],
            'propagate': True,
        },

        # 4 пункт задания
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True,
        },

        # 5, 3 пункт задания
        'django.request': {
            'handlers': ['file_errors', 'file_critical', 'mail_admin'],
            'propagate': True,
        },

        # 5, 3 пункт задания
        'django.server': {
            'handlers': ['file_errors', 'file_critical', 'mail_admin'],
            'propagate': True,
        }
    }
}
