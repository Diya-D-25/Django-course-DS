from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")


def counter(request):
    words = request.GET["sentence"]
    number = len(words.split())
    context = {"words": number}
    return render(request, "count.html", context)
