from django.shortcuts import render
from django.http import *
# Create your views here.

def index(request):
    """
    This is the main request of the home app
    which merely represents the home page of
    the project.
    """
    return render(request, 'home/index.html', content_type="text/html")

