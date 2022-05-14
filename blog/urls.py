from django.urls import path
from .views import Home, Contact

app_name = 'blog'
urlpatterns = [
    # post views
    path('', Home.as_view(), name='blog_list'),
    path('contact', Contact.as_view(), name='contact'),
    # path('<slug:slug>/', Home.as_view(), name='blog_detail'),
]
