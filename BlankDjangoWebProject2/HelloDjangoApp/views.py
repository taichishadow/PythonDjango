from django.shortcuts import render
from HelloDjangoApp import models
from django.http import JsonResponse
from datetime import datetime
from HelloDjangoApp.models import Role, User
from django.core import serializers

# Create your views here.
def getRoles(request):
    roles = Role.objects.all().values('name')
    roles_list = list(roles) 
    return JsonResponse(roles_list, safe=False)

def index(request):
    now = datetime.now()
    
    return render(
        request, 
         "HelloDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title': "this is a test project",
            'message': "Hello Django! on ",
            'content': now.strftime("%A, %d %B, %Y at %X"),
        }
    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title': "about me",
            'content': "this is about me page",
        }
    )
