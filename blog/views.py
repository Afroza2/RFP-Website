from django.db.models.functions import ExtractYear, TruncMonth
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView
from django.http import Http404
from .models import Post, Report, News, Member, Project, Gallery, About, Video, NewList, FList
from django.db.models import Q, Count
from taggit.models import Tag
from django.views.generic.dates import YearArchiveView



# , Report, Gallery

class TagMixin(object):
    def get_context_data(self, **kwargs):
        data = super(TagMixin, self).get_context_data(**kwargs)
        data['tags'] = Tag.objects.all()
        return data


class NewsListView(TagMixin, ListView):
    model = News
    queryset = News.objects.all()
    context_object_name = 'newss'
    template_name = 'blog/news.html'


class NewsDetailView(TagMixin, DetailView):
    model = News
    date_field = "nw_publish"
    context_object_name = 'news'
    template_name = 'blog/news_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['news_details_view'] = News.objects.all()
        data['news_years'] = News.objects.annotate(year=ExtractYear('nw_publish')).values('year').annotate(
            total_entries=Count('year')).order_by()
        # .annotate(sum=Sum('news_title')).values('year', 'sum')
        data['news_years'] = (
            News.objects.values(month=TruncMonth('nw_publish'))
                .annotate(total_entries=Count('month'))
                .order_by()
        )
        return data


class NewsMonths(ListView):
    model = News
    # context_object_name = 'posts-by-month'
    template_name = 'blog/newsarchive.html'

    def get_queryset(self, *args, **kwargs):
        return (
            super().get_queryset(*args, **kwargs).filter(
                nw_publish__year=self.kwargs['year'],
                nw_publish__month=self.kwargs['month'], )
        )


class NewsTagView(TagMixin, ListView):
    model = News
    context_object_name = 'newss'
    template_name = 'blog/news.html'

    def get_queryset(self):
        return News.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


class NewsYearArchiveView(YearArchiveView):
    context_object_name = 'news_years'
    date_field = "nw_publish"
    year_format = '%Y'
    make_object_list = True
    allow_future = True
    queryset = News.objects.filter(nw_status='published').order_by('nw_publish', 'news_title')


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


# class ArchiveYearView(YearArchiveView):
#     model = Report
#     template_name = 'blog/archive_year.html'
#     context_object_name = 'archive_list'
#     make_object_list = True
#     allow_future = True


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


# class NewListView(ListView):
#     model = NewList
#     template_name = 'blog/newcommittee.html'

#     context_object_name = 'members'

#     # def get_queryset(self):

#     #     queryset = NewList.objects.order_by('order','position')
#     #     print(queryset)  # Add this line to check the queryset in the console
#     #     return queryset
    
class NewListView(ListView):
    model = NewList
    template_name = 'blog/newcommittee.html'
    context_object_name = 'members'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     # Define custom order of positions
    #     position_order = [
    #         "President", "Vice President", "General Secretary", "Joint Secretary",
    #         "Assistant Secretary", "Treasurer", "Organizing Secretary", "Office Secretary",
    #         "Media and Communications Secretary", "Secretary of Child Education and Protection",
    #         "Human Resource Development", "Secretary", "Hill-tracks and Tribal Affairs Secretary",
    #         "Women's Affairs Secretary", "Executive", "Members"
    #     ]

    #     context['position_order'] = position_order
    #     return context

    def get_queryset(self):
        return NewList.objects.order_by('order')
   

class FormerListView(ListView):
    model = FList
    context_object_name = 'former_committee'
    template_name = 'blog/fcommittee.html'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'blog/project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'blog/project_detail.html'
