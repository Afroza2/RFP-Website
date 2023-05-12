from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView
from django.http import Http404
from .models import Post, Report, News, Member, Project, Gallery, About, Video, FC
from django.db.models import Q
from django.views.generic.dates import YearArchiveView
from taggit.models import Tag


# , Report, Gallery

class TagMixin(object):
    def get_context_data(self, **kwargs):
        data = super(TagMixin, self).get_context_data(**kwargs)
        data['news_tags'] = Tag.objects.all()
        return data


class NewsListView(ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = 'newss'
    template_name = 'blog/news.html'


class NewsTagView(ListView):
    model = News
    context_object_name = 'newss'
    template_name = 'blog/news.html'

    def get_queryset(self):
        return News.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


class SearchView(TemplateView):
    template_name = 'blog/search_results.html'
    model = News, Report, Project

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = (News.objects.filter(news_title__icontains=q) or
                        Report.objects.filter(rp_title__icontains=q) or Project.objects.filter(pr_title__icontains=q))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # print("result", super().get_context_data(results=zip(self.news_results, self.rp_results)))
        return super().get_context_data(results=self.results, **kwargs)


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'blog/news_detail.html'


class AboutDetail(ListView):
    model = About
    context_object_name = 'about'
    template_name = 'blog/about.html'


class Home(ListView):
    model = Post
    context_object_name = 'home'
    template_name = 'blog/home.html'

    # def get_queryset(self):
    #     q = self.request.GET.get('q')
    #     if q:
    #         object_list = News.objects.filter(
    #             Q(news_title__icontains=q)
    #         )
    #     else:
    #         object_list = News.objects.all()
    #
    #     return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['news_data_home1'] = News.objects.all()
        data['news_data_home2'] = News.objects.all()[1:4]
        data['photo_home'] = Gallery.objects.all()
        data['video_home'] = Video.objects.all()
        data['home_post'] = Post.objects.all()
        return data

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #
    #     return data


class HomeDetail(generic.DetailView):
    model = Post
    context_object_name = 'details'
    template_name = 'blog/details.html'


class ReportListView(ListView):
    model = Report
    queryset = Report.objects.all()
    context_object_name = 'reports'
    template_name = 'blog/report_list.html'


class ReportTagView(ListView):
    model = Report
    context_object_name = 'reports'
    template_name = 'blog/report_list.html'

    def get_queryset(self):
        return Report.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
        # return Report.objects.filter(tags__name__in=[self.kwargs['tag']])


class ReportYearArchiveView(YearArchiveView):
    queryset = Report.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True


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
class PhotoGallery(ListView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'blog/photo.html'


class VideoGallery(ListView):
    model = Video
    context_object_name = 'video'
    template_name = 'blog/video.html'


class FCListView(ListView):
    model = FC
    context_object_name = 'former_committee'
    template_name = 'blog/fcommitte.html'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'blog/project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'blog/project_detail.html'
