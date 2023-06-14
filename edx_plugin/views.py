from django.http import HttpResponse


# test response
def get_plugin_page(request):
    return HttpResponse("This is plugin page")
