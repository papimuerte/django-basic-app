from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to Django!</h1><p>This is a basic Django application.</p>")
