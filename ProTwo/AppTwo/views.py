from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html")

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict ={'users':user_list}
    return render(request, "AppTwo/users.html", context = user_dict)

def help(request):
    dict = {"insert_me":"Help page"}
    return render(request,'AppTwo/help.html', context = dict)
