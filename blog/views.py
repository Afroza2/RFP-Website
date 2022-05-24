from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post, Report, Gallery


class Home(ListView):
    model = Post
    context_object_name = 'home'
    template_name = 'blog/home.html'


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'
    template_name = 'blog/report_list.html'


class ReportDetailView(DetailView):
    model = Report
    slug_field = 'report_slug'
    context_object_name = 'report'
    template_name = 'blog/report_detail.html'


class Contact(ListView):
    model = Post
    context_object_name = 'contact'
    template_name = 'blog/contact.html'


class Gallery(ListView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'blog/photo.html'
