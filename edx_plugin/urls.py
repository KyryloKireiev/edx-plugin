"""
URLs for edx_plugin.
"""
from django.urls import path, re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .views import get_test_plugin

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'^plugin', TemplateView.as_view(template_name="edx_plugin/base.html")),
    path('test_plugin_response/', get_test_plugin, name='test_plugin'),
]
