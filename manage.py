#!/usr/bin/env python
import os
import sys

from hometool.libs.commons.utils import get_default_django_settings_module


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')
    # NOTE: instead of changing the DJANGO_CONFIGURATION class for each environment we change the DJANGO_SETTINGS_MODULE
    # and keep the same class (i.e. Settings) for all environments.
    #
    # So instead of having classes like 'Common', 'Production', 'Dev' in the module 'hometool.settings',
    # We would have class 'Settings' in modules 'hometool.settings.common', 'hometool.settings.production', 'hometool.settings.dev',
    # 'hometool.settings.qa', 'hometool.settings.local' etc.

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
