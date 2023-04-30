from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('topic inserted successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}




    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('webpage inserted successfully')
    return render(request,'insert_webpage.html',d)



        


    return render(request,'insert_webpage.html')