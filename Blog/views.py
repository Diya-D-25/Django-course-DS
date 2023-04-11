from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return HttpResponse("Hello World")


def blog(request):
    return HttpResponse("Blog Home")
