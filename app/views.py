from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'topics':ETFO}
    if request.method == 'POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic are inserted Successfully....')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'webpages':EWFO}
    if request.method == 'POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('Webpage is Created successfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EARFO=AccessRecordForm()
    d={'accessrecords':EARFO}
    if request.method == 'POST':
        ARFDO=AccessRecordForm(request.POST)
        if ARFDO.is_valid():
            ARFDO.save()
            return HttpResponse('AccessRecord is inserted Successfully...')
    return render(request,'insert_accessrecord.html',d)