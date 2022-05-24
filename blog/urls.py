from django.urls import path

from .views import Home, Contact, ReportListView, ReportDetailView, Gallery

app_name = 'blog'
urlpatterns = [
    # post views
    path('', Home.as_view(), name='blog_list'),
    path('contact', Contact.as_view(), name='contact'),
    path('photo-gallery', Gallery.as_view(), name='gallery'),
    path('reports', ReportListView.as_view(), name='resources'),
    path('<rp_slug>', ReportDetailView.as_view(), name='report_detail'),
]
