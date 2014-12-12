import imp

def get_default_django_settings_module():
    try:
        file_ = imp.find_module('local', ['hometool/settings'])[0]
    except ImportError:
        default_django_settings_module = "hometool.settings.common"
    else:
        default_django_settings_module = "hometool.settings.local"
        file_.close()
    return default_django_settings_module

