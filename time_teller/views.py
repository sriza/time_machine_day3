from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def home(request):
    return HttpResponse('Welcome to time machine!')

def today(request):
    return HttpResponse(datetime.datetime.today().date())

def times(request):
    return HttpResponse(datetime.datetime.now().timestamp())