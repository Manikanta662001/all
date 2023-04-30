from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':400,'b':300,'c':100}
    return render(request,'condition.html',d)