# blog/urls.py
from django.urls import path
from .views import (
    Home, HomeDetail, Contact, ReportListView,  NewsListView,
    NewsDetailView, MemberListView, ProjectListView, ProjectDetailView,
    SearchView, PhotoGallery, AboutDetail, VideoGallery,
    NewListView, ReportTagView, NewsTagView, FormerListView
)
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
    path('home/<slug:slug>/', HomeDetail.as_view(), name='details'),
    path('about/', AboutDetail.as_view(), name='about'),
    path('members/', MemberListView.as_view(), name='members'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('photo-gallery/', PhotoGallery.as_view(), name='gallery'),
    path('video-gallery/', VideoGallery.as_view(), name='video'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('report/<slug:tag_slug>/', ReportTagView.as_view(), name='report_tag'),
    # path('archive/<int:year>/', ArchiveYearView.as_view(), name='archive_year'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/taggit/tag/<slug:tag_slug>/', NewsTagView.as_view(), name='news_tag'),
    path('new-committee/', NewListView.as_view(), name='new_committee'),
    path('former-committee/', FormerListView.as_view(), name='former_committee'),
    path('rfp-families/', RedirectView.as_view(url='https://www.rfp.org/where-we-work/'), name='rfp_families'),
    path('contact/', Contact.as_view(), name='contact'),
]
