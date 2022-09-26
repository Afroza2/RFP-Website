from django.urls import path, re_path

from . import views
from .views import Home, HomeDetail, Contact, ReportListView, ReportDetailView, NewsListView, NewsDetailView, \
    MemberListView, ProjectListView, ProjectDetailView

# , Gallery

app_name = 'blog'
urlpatterns = [
    # post views
    path('', Home.as_view(), name='home'),
    path('home/<slug:slug>/', HomeDetail.as_view(), name='details'),
    path('members/', MemberListView.as_view(), name='members'),
    # path('photo-gallery', Gallery.as_view(), name='gallery'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('report/<slug:slug>/', ReportDetailView.as_view(), name='report_detail'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('taggit/tag/<slug:tag_slug>/', NewsListView.as_view(), name='post_tag'),
    # path('blognews/', HomeNewsList.as_view(), name='home_news_list'),
    # path('blognews/<slug:slug>/', HomeNewsDetailsView.as_view(), name='home_news_detail'),
    path('contact/', Contact.as_view(), name='contact'),
]
