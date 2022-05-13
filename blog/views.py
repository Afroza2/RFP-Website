from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post


class Home(ListView):
    model = Post
    context_object_name = 'home'
    template_name = 'blog/home.html'
