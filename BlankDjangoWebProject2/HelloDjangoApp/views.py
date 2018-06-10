from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime

# Create your views here.
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
