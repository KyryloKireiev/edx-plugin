def plugin_settings(settings):
    # Update the provided settings module with any app-specific settings.
    settings.FEATURES['ENABLE_MY_APP'] = True
    settings.PLUGIN_PAGE_URL = "/plugin_page/"
