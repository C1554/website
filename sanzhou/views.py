from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def hchart(request):
    return render(request,'hchart.html')

