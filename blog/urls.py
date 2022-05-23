from django.urls import path
from .views import Home, Contact, Report

app_name = 'blog'
urlpatterns = [
    # post views
    path('', Home.as_view(), name='blog_list'),
    path('contact', Contact.as_view(), name='contact'),
    path('resources', Report.as_view(), name='resources'),
    # path('<slug:slug>/', Home.as_view(), name='blog_detail'),
]
