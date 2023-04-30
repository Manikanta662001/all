from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':22,'b':20,'c':30}
    return render(request,'a1_first.html',d)
def a1_second(request):
    d={'a':22,'b':20,'c':10}
    return render(request,'a1_second.html',d)