from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticS3BotoStorage(S3BotoStorage):

    def url(self, name):
        url = super(StaticS3BotoStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        # Work-around to force browsers to always load newer versions of static files
        #return url
        return "%s?%s" % (url, settings.RESOURCE_VERSION)