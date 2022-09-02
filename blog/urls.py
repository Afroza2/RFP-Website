from django.urls import path, re_path

from . import views
from .views import Home, Contact, ReportListView, ReportDetailView\
    # , Gallery

app_name = 'blog'
urlpatterns = [
    # post views
    path('', Home.as_view(), name='home'),
    path('<slug:slug>/', views.HomeDetail.as_view(), name='details'),
    path('contact', Contact.as_view(), name='contact'),
    # path('photo-gallery', Gallery.as_view(), name='gallery'),
    path('reports', ReportListView.as_view(), name='report_list'),
    path('<slug:slug>', ReportDetailView.as_view(), name='report_detail'),
]
