from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from app1.models import *
def first(request):
    if request.method=='POST': 
        username=request.POST['un']
        password=request.POST['pw']
        return HttpResponse('data is submitted')
    return render(request,'first.html')


def inserttopic(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('insertion is done')
    return render(request,'inserttopic.html')


def insertwebpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
    return render(request,'insertwebpage.html',d)

def insertar(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        name=request.POST['n']
        date=request.POST['date']
        author=request.POST['aut']
        wo=Webpage.objects.get(name=n)
        AR=AccessRecord.objects.get_or_create(name=wo,date=date,author=author)
        AR.save()
    return render(request,'insertar.html',d)


def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        RWOS=Webpage.objects.none()
        for i in MSTS:
            RWOS=RWOS|Webpage.objects.filter(topic_name=i)
        d1={'RWOS':RWOS}
        return HttpResponse('retrive is done')
    return render(request,'retrive_webpage.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)
