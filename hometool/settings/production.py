import os
from . import common


class Settings(common.Settings):
    ########## DEBUG CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = False

    ########## APPS CONFIGURATION
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    THIRD_PARTY_APPS = common.Settings.THIRD_PARTY_APPS + (
        'storages',
        'collectfast',
    )
    ########## END APPS CONFIGURATION

    ########## STORAGE CONFIGURATION
    STATICFILES_STORAGE = 'libs.commons.s3.StaticS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

    # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
    AWS_STORAGE_BUCKET_NAME = ''
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = False

    AWS_S3_CUSTOM_DOMAIN = ''
    AWS_S3_SECURE_URLS = False
    CF_DISTRIBUTION_ID = 'E2PTDVN03D1QSX'

    AWS_IS_GZIPPED = True
    AWS_PRELOAD_METADATA = True
    GZIP_CONTENT_TYPES = (
        'text/html',
        'text/css',
        'application/javascript',
        'application/x-javascript',
        'text/javascript'
    )

    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIRY = 60 * 60 * 24 * 7
    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY,
            AWS_EXPIRY)
    }

    ########## END STORAGE CONFIGURATION

    ####### DOMAIN SETTINGS
    ENV_CONFIG = {
    }
