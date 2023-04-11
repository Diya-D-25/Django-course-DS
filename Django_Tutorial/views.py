from django.shortcuts import render


def home_page(request):
    context = {"title": "Home Page"}
    return render(request, "home.html", context)


def counter(request):
    words = request.GET["sentence"].split()
    number = len(words)
    context = {"numbers": number, "title": "Count", "words": words}
    return render(request, "count.html", context)
