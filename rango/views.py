from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = 'Rango says hey there world!';
    response += '<br>';
    response += '<a href="about">See what Rango is about.</a>';
    return HttpResponse(response)

def about(request):
    response = 'Rango says here is the about page.';
    response += '<br>';
    response += '<a href="./">Back to index.</a>';
    return HttpResponse(response)
