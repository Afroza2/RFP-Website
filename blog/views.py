from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView
from django.http import Http404
from .models import Post, Report, News, Member, Project
from django.db.models import Q


# , Report, Gallery
class NewsListView(ListView):
    model = News
    context_object_name = 'newss'
    template_name = 'blog/news.html'


class SearchView(TemplateView):
    template_name = 'blog/search_results.html'
    model = News

    # def get_queryset(self):
    #     name = self.kwargs.get('name', '')
    #     object_list = self.model.objects.all()
    #     if name:
    #         object_list = object_list.filter(name__icontains=name)
    #     return object_list

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = News.objects.filter(news_title__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, **kwargs)


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'blog/news_detail.html'


class Home(ListView):
    model = Post
    context_object_name = 'home'
    template_name = 'blog/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['news_data_home'] = News.objects.all()
        return data


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


class MemberListView(ListView):
    model = Member
    context_object_name = 'member'
    template_name = 'blog/members.html'


class Contact(ListView):
    model = Post
    context_object_name = 'contact'
    template_name = 'blog/contact.html'


#
# class Gallery(ListView):
#     model = Gallery
#     context_object_name = 'gallery'
#     template_name = 'blog/photo.html'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'blog/project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'blog/project_detail.html'
