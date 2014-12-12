"""Common settings and globals."""

from os.path import abspath, basename, dirname, join, normpath
from sys import path

from .logger_settings import LoggerSettingsMixin
from configurations import Configuration

class Settings(LoggerSettingsMixin, Configuration):
    ########## PATH CONFIGURATION
    # Absolute filesystem path to the Django project directory:
    DJANGO_ROOT = dirname(dirname(abspath(__file__)))

    # Absolute filesystem path to the top-level project folder:
    SITE_ROOT = dirname(DJANGO_ROOT)

    # Site name:
    SITE_NAME = basename(DJANGO_ROOT)

    # Add our project to our pythonpath, this way we don't need to type our project
    # name in our dotted import paths:
    path.append(DJANGO_ROOT)
    ########## END PATH CONFIGURATION

    ########## DEBUG CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = True
    ########## END DEBUG CONFIGURATION

    ########## MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('Your Name', 'your_email@example.com'),
    )
    ########## END MANAGER CONFIGURATION

    ########## GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'America/Chicago'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'en-us'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = False

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = False

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = False  # Default is False, but, purposefully made False to track it
    ########## END GENERAL CONFIGURATION

    ########## MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    ########## END MEDIA CONFIGURATION

    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))
    STATICPAGES_ROOT = normpath(join(DJANGO_ROOT, 'staticpages'))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        normpath(join(DJANGO_ROOT, 'assets')),
        STATICPAGES_ROOT
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
    )
    ########## END STATIC FILE CONFIGURATION

    ########## SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = r"dx-nepz+v0d_yhs(eyymipy!fti*m#-)wz*w4lcz%!4u&6tks="
    ########## END SECRET CONFIGURATION

    ########## TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        #'django.contrib.auth.context_processors.auth',
        #'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        #'django.core.context_processors.tz',
        #'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        normpath(join(DJANGO_ROOT, 'templates')),
    )
    ########## END TEMPLATE CONFIGURATION

    ########## MIDDLEWARE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
    MIDDLEWARE_CLASSES = (
        # Default Django middleware.
        'django.middleware.common.CommonMiddleware',
        #'django.contrib.sessions.middleware.SessionMiddleware',
        #'django.middleware.csrf.CsrfViewMiddleware',
        #'django.contrib.auth.middleware.AuthenticationMiddleware',
        #'django.contrib.messages.middleware.MessageMiddleware',
    )
    ########## END MIDDLEWARE CONFIGURATION

    ########## URL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
    ROOT_URLCONF = '{0}.urls'.format(SITE_NAME)
    ########## END URL CONFIGURATION

    ########## APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        #'django.contrib.auth',
        #'django.contrib.contenttypes',
        #'django.contrib.sessions',
        #'django.contrib.sites',
        #'django.contrib.messages',
        'django.contrib.staticfiles',

        # Admin panel and documentation:
        #'django.contrib.admin',
        #'django.contrib.admindocs',
    )

    THIRD_PARTY_APPS = ()

    LOCAL_APPS = (
        'libs.commons',
    )

    ########## END APP CONFIGURATION

    ########## CACHE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'project-default'
        }
    }
    ########## END CACHE CONFIGURATION

    ########## STORAGE SETTINGS
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    ########## END STORAGE SETTINGS

    RESOURCE_VERSION = '2'

    STATICPAGES_MANIFEST = 'staticpages_manifest.json'

    ####### DOMAIN SETTINGS
    ENV_CONFIG = {}
    MAIN_CONFIG = {
        'resource_version': RESOURCE_VERSION,
    }

    ########## DEPENDANT SETTINGS
    CONFIG = (property(lambda self: dict(self.MAIN_CONFIG, **self.ENV_CONFIG)))

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = property(lambda self: self.DJANGO_APPS + self.THIRD_PARTY_APPS + self.LOCAL_APPS)

    ######### END DEPENDANT SETTINGS

