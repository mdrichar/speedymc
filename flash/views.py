from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json

def index(request):
    return HttpResponse("Trying to run this here and there, plus live modifications.")

# Create your views here.
