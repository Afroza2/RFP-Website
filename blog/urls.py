from django.urls import path
from .views import Home, Contact, Report, Gallery

app_name = 'blog'
urlpatterns = [
    # post views
    path('', Home.as_view(), name='blog_list'),
    path('contact', Contact.as_view(), name='contact'),
    path('resources', Report.as_view(), name='resources'),
    path('photo-gallery', Gallery.as_view(), name='gallery')
    # path('<slug:slug>/', Home.as_view(), name='blog_detail'),
]
