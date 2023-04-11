from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_page, name="blog-home"),
    path("blog/", views.blog, name="blog"),
]
