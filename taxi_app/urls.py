from django.urls import path
from django.http import HttpResponse
from .views import *

def test(request):
    return HttpResponse("ok report")

urlpatterns = [
    path('a', test),
    path('',home),
]
