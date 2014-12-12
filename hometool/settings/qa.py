from . import production


class Settings(production.Settings):

    # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
    AWS_STORAGE_BUCKET_NAME = ''
    AWS_S3_CUSTOM_DOMAIN = ''
    CF_DISTRIBUTION_ID = 'TBD'

    ####### DOMAIN SETTINGS
    ENV_CONFIG = {
    }
