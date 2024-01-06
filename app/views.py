from django.shortcuts import render
from app.models import *
from app.forms import*
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()

            return HttpResponse('insert_topic done successfully')
    return render(request,'insert_topic.html',d)        


def insert_webpage(request):
    EWFO=webpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=webpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            
            return HttpResponse('insert_webpage done ')
    return render(request,'insert_webpage.html',d)        


def insert_accessrecord(request):
    EAFO=accessrecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=accessrecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            
            return HttpResponse('insert_Acessrecord done ')
    return render(request,'insert_accessrecord.html',d)        