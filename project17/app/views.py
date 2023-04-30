from django.shortcuts import render

# Create your views here.


def bootstrap4(request):
    return render(request,'bootstrap4.html')