from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts


# Create your views here.
def home_page(request):
    context = {"posts": Posts.objects.all()}
    return render(request, "blogs.html", context)


def blog(request):
    return HttpResponse("Blog Home")
