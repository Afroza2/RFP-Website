from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Post, Report


# , Report, Gallery


class Home(ListView):
    model = Post
    context_object_name = 'home'
    template_name = 'blog/home.html'


class HomeDetail(generic.DetailView):
    model = Post
    context_object_name = 'details'
    template_name = 'blog/details.html'


class ReportListView(ListView):
    model = Report
    context_object_name = 'reports'
    template_name = 'blog/report_list.html'


#     # def get_object(self, queryset=None):
#     #     return Report.objects.get(rp_slug=self.kwargs.get("rp_slug"))
#
#
class ReportDetailView(DetailView):
    model = Report
    # slug_field = 'slug'
    context_object_name = 'report'
    template_name = 'blog/report_detail.html'


#
#     def get_object(self):
#         return get_object_or_404(Report, id=self.kwargs['pk'])
#

class Contact(ListView):
    model = Post
    context_object_name = 'contact'
    template_name = 'blog/contact.html'

#
# class Gallery(ListView):
#     model = Gallery
#     context_object_name = 'gallery'
#     template_name = 'blog/photo.html'
