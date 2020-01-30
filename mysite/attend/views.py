from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def attendance(request):
    return HttpResponse("This is attendance page.")

def id_archive(request,id):
    return HttpResponse("This is id : %d" % id)