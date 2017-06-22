from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("AppTwo")

def help(request):
    dict = {"insert_me":"Help page"}
    return render(request,'AppTwo/help.html', context = dict)
