import os
import logging

from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.test.client import RequestFactory

import urls
import json

logger = logging.getLogger('commands.collectpages')

page_storage = FileSystemStorage(location=settings.STATICPAGES_ROOT)

class Command(BaseCommand):

    def handle(self, *args, **options):
        manifest_file_path = settings.STATICPAGES_MANIFEST
        request_factory = RequestFactory()
        manifest_list = []
        for page in urls.urlpatterns:
            page_name = page.name
            logger.info("Retrieving : %s" % page_name)
            request = request_factory.get(reverse(page_name, args=()))
            response = page.callback(request).render()
            path = os.path.join(request.path.strip("/"), "index.html")
            logger.info("Writing    : %s" % path)
            if page_storage.exists(path):
                logger.info("Deleting    : %s" % path)
                page_storage.delete(path)
            page_storage.save(path, ContentFile(response.content))
            manifest_list.append(request.path)

        #Save the manifest file
        if page_storage.exists(manifest_file_path):
                logger.info("Deleting    : %s" % manifest_file_path)
                page_storage.delete(manifest_file_path)
        page_storage.save(manifest_file_path, ContentFile(json.dumps(manifest_list)))

