from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('This is our first view function')
def propose(request):
    return HttpResponse('<marquee>yes i have some work</marquee>')
def reject(request):
    return HttpResponse('<h1>hai friends</h1>')
