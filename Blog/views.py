from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Emmanuel",
        "content": "This is the post content",
        "title": "Post Title Supreme",
        "Posted_Date": "Today",
    },
    {
        "author": "Author_2",
        "content": "This is the Another post here",
        "title": "Post Title here",
        "Posted_Date": "Yesterday",
    },
]


# Create your views here.
def home_page(request):
    context = {"posts": posts}
    return render(request, "blogs.html", context)


def blog(request):
    return HttpResponse("Blog Home")
