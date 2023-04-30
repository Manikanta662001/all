from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'a2_first.html',d)
def a2_second(request):
    d={'name':'manikanta'}
    return render(request,'a2_second.html',d)