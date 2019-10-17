from django.http import HttpResponse
from django.shortcuts import render


# /products -> index
# Uniform resource locator
def index(request): # main page of our app
    return HttpResponse('Hello World')  # returns object to our function

def new(request):
    return HttpResponse('Welcome to new page')

