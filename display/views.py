from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'display/index.html/')

def spread(request):
    return HttpResponse("spread")

def deathrate(request):
    return HttpResponse("deathrate")