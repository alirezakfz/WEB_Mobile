from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : {}</p> 
<p>Request Method : {}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

# def index(request): 
#     return HttpResponse("Hello, world. This is the index view of Demoapp.")


def say_goodbye(request):
    return HttpResponse("Goodbye ..........")

def homepage(request):
    return HttpResponse("This is the home Page")