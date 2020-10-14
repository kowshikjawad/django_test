from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me':"hello I am from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)

def help(request):
    return render(request,"first_app/help.html",)

# Create your views here.
