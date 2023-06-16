import logging
from path import Path


RG_CUSTOMIZATIONS_DIR = Path(__file__).parent.parent
log = logging.getLogger(__name__)


def plugin_settings(settings):
    # Update the provided settings module with any app-specific settings.
    settings.FEATURES['ENABLE_MY_APP'] = True
    settings.PLUGIN_PAGE_URL = "/plugin_page/"
    settings.MAKO_TEMPLATE_DIRS_BASE.append(RG_CUSTOMIZATIONS_DIR / 'templates')
    log.warning('[RG]: settings override! (MAKO_TEMPLATE_DIRS_BASE)')
