from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome to my HomePage!!")


def write(request):
    return HttpResponse("<h1>Create your Blog!!</h1>")
