from django.http import HttpResponse
from common.djangoapps.edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.programs.models import ProgramsApiConfig
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.utils.translation import gettext as _


# test response
def get_test_plugin(request):
    return HttpResponse(_("This is test plugin page"))


@login_required
@require_GET
def get_plugin_page(request):
    programs_config = ProgramsApiConfig.current()
    context = {
        'disable_courseware_js': True,
        'nav_hidden': True,
        'show_dashboard_tabs': True,
        'show_program_listing': programs_config.enabled,
        'uses_bootstrap': True,
    }
    return render_to_response('edx_plugin/plugin_page.html', context)
