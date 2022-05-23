from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post, Report


class Home(ListView):
    model = Post
    context_object_name = 'home'
    template_name = 'blog/home.html'


class Report(ListView):
    model = Report
    report_list = Report.objects.all()
    context_object_name = 'resources'
    template_name = 'blog/resources.html'


class Contact(ListView):
    model = Post
    context_object_name = 'contact'
    template_name = 'blog/contact.html'
