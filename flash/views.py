from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import QuestionSet, BinaryFact, ResponseTiming, Bout, User
import json

def index(request):
    return HttpResponse("Trying to run this here and there, plus live modifications.")

def listing(request):
    #factoid_listing = Factoid.objects.all()
    factoid_listing = BinaryFact.objects.all()
    template = loader.get_template('flash/listing.html')
    context = {
        'factoid_listing' : factoid_listing, 
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
