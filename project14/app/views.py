from django.shortcuts import render

# Create your views here.


def msd_img(request):
    return render(request,'msd_img.html')