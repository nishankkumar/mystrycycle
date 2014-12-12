import logging

from django.core.management.base import BaseCommand
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import json
import boto

logger = logging.getLogger('commands.invalidatecf')

page_storage = FileSystemStorage(location=settings.STATICPAGES_ROOT)

class Command(BaseCommand):

    def handle(self, *args, **options):
        manifest_file_path = settings.STATICPAGES_MANIFEST
        paths = []
        manifest_file = page_storage.open(manifest_file_path)
        paths = json.loads(manifest_file.read())
        manifest_file.close()

        logger.info("Invalidating    : %s" % paths)
        cf = boto.connect_cloudfront()
        cf.create_invalidation_request(settings.CF_DISTRIBUTION_ID, paths)


