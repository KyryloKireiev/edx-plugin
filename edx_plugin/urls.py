"""
URLs for edx_plugin.
"""
from django.urls import path, re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from views import get_plugin_page

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="edx_plugin/base.html")),
    path('plugin/', get_plugin_page, name='edx_plugin'),
]
