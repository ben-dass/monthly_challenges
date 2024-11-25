from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("View return from challenges!")
