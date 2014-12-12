from django.template import Library
from django.conf import settings

register = Library()

@register.simple_tag
def config(name):
    return settings.CONFIG.get(name)