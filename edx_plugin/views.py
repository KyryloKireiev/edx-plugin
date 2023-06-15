from django.http import HttpResponse


# test response
def get_test_plugin(request):
    return HttpResponse("This is plugin page")
