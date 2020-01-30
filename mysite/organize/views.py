from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def organize(request):
    return HttpResponse("This is organize page.")