from django.urls import path, re_path

from . import views
from .views import Home, HomeDetail, Contact, ReportListView, ReportDetailView, NewsListView, NewsDetailView, \
    MemberListView, ProjectListView, ProjectDetailView, SearchView, ReportYearArchiveView, PhotoGallery, AboutDetail, \
    VideoGallery, FCListView, ReportTagView, NewsTagView, NewsYearArchiveView, NewsMonths
from django.views.generic.base import RedirectView

# , Gallery

app_name = 'blog'
urlpatterns = [
    # post views

    path('', Home.as_view(), name='home'),
    path("search", SearchView.as_view(), name='search'),
    path('home/<slug:slug>/', HomeDetail.as_view(), name='details'),
    path('about/', AboutDetail.as_view(), name='about'),
    path('members/', MemberListView.as_view(), name='members'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('photo-gallery/', PhotoGallery.as_view(), name='gallery'),
    path('video-gallery/', VideoGallery.as_view(), name='video'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('report/<slug:slug>/', ReportDetailView.as_view(), name='report_detail'),
    # path('report/<int:year>/', ReportYearArchiveView.as_view(), name="report_year_archive"),
    path('report/taggit/tag/<slug:tag_slug>/', ReportTagView.as_view(), name='report_tag'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/taggit/tag/<slug:tag_slug>/', NewsTagView.as_view(), name='post_tag'),
    # path('news/<int:year>/<int:month>/', NewsMonths.as_view(), name='posts-by-month'),
    path('former-committee/', FCListView.as_view(), name='former-committee'),
    path('rfp-families/', RedirectView.as_view(url='https://www.rfp.org/where-we-work/')),
    # path('blognews/', HomeNewsList.as_view(), name='home_news_list'),
    # path('blognews/<slug:slug>/', HomeNewsDetailsView.as_view(), name='home_news_detail'),
    path('contact/', Contact.as_view(), name='contact'),
]
