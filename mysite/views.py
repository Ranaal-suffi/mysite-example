from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world!')

def two(request):
    return HttpResponse ("Hi Ameer")