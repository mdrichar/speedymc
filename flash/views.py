from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import QuestionSet, BinaryFact, ResponseTiming, Bout
from django.contrib.auth.models import User
from django.db import connection
import json

def index(request):
    return HttpResponse("Trying to run this here and there, plus live modifications.")

def listing(request):
    #factoid_listing = Factoid.objects.all()
    factoid_listing = BinaryFact.objects.all()
    template = loader.get_template('flash/listing.html')
    context = {
        'factoid_listing' : factoid_listing, 
	'logged_in_user' : request.user,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.

def subsetq(request):
    print(request.POST)
    items = dict(request.POST.lists())
    qs = QuestionSet()
    qs.name = items['setname'][0]
    qs.description = items['setdesc'][0]
    print("items: ", items['problem'])
    setdesc = request.POST.get('setdesc')
    qs.save()
    print("setdesc: ", setdesc)
    for ids in items['problem']: 
        print('Selected',ids)
        bf = BinaryFact.objects.filter(pk=ids)[0]
        qs.binary_facts.add(bf)
    qs.save()

    return HttpResponse("New question set created: ", qs.id)

def jsonlisting(request):
    qset_id = request.GET['qset']
    print("jsonlisting got called with qset ", qset_id )
    factoid_listing = BinaryFact.objects.filter(qsets__id=qset_id).order_by('?')
    to_json = []
    for factoid in factoid_listing:
        fact_dict = {}
        fact_dict['id'] = factoid.id
        fact_dict['f1'] = factoid.operand1
        fact_dict['f2'] = factoid.operand2
        to_json.append(fact_dict)
    response_data = json.dumps(to_json)
    return HttpResponse(response_data)

def timingListing(request):
    qset_id = request.GET['qset']
    user_id = request.GET['user']
    print("timingListing got called with qset ", qset_id, user_id )
    to_json = []
    with connection.cursor() as cursor:
        cursor.execute("select au.username, question_set_id, fb.id, fb.elapsed from auth_user as au, flash_bout as fb where fb.user_id=au.id and question_set_id=%s and au.id=%s; ", [qset_id, user_id])
        to_json.append(cursor.fetchall())
    response_data = json.dumps(to_json)
    return HttpResponse(response_data)

def postBout(request):
    print("Post Bout")
    print(request.POST['jsons'])
    print(request.POST['qset_id'])
    jsonitems = json.loads(request.POST['jsons'])
    total_elapsed = 0
    if len(jsonitems) > 0:
        bout = Bout()
        bout.user = User.objects.filter(id=request.user.id)[0]
        bout.question_set = QuestionSet.objects.filter(id=request.POST['qset_id'])[0]
        bout.save()
        for fact in jsonitems:
            if 'elapsed' in fact:
                print(fact)
                rt = ResponseTiming()
                rt.bout = bout
                rt.binary_fact = BinaryFact.objects.filter(pk=fact['id'])[0]
                rt.elapsed = fact['elapsed']
                total_elapsed += rt.elapsed
                rt.save()
        bout.elapsed = total_elapsed
        bout.correct_cnt = len(jsonitems)
        bout.save()
    #print(jsonitems)
    return HttpResponse()

def postarg(request):
    #fact = request.POST['fact']
    print("Got called" + str(request.POST['fact[elapsed]']))
    rt = ResponseTiming()
    #bout = Bout.objects.filter(pk=request.POST['bout'])
    bout = Bout.objects.filter(pk=3)[0]
    rt.bout = bout
    rt.binary_fact = BinaryFact.objects.filter(pk=request.POST['fact[id]'])[0]
    rt.elapsed = request.POST['fact[elapsed]']
    rt.save()
    return HttpResponse([])

def iterlist(request):
    template = loader.get_template('flash/iterlist.html')
    qsets = QuestionSet.objects.all()
    context = {
	'qset_listing' : qsets
    }
    return HttpResponse(template.render(context,request))

def topscores(request):
    template = loader.get_template('flash/topscores.html')
    timings = ResponseTiming.objects.all()
    user_listing = User.objects.all()
    qsets = QuestionSet.objects.all()
    context = {
	'timing_listing' : timings,
	'user_listing' : user_listing,
	'qset_listing' : qsets
    }
    return HttpResponse(template.render(context,request))

def selgrid(request):
   template = loader.get_template('flash/selgrid.html')
   context = {}
   return HttpResponse(template.render(context,request))


# Create your views here.
