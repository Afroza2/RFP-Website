from django.urls import path
from .views import Home

app_name = 'blog'
urlpatterns = [
    # post views
    path('', Home.as_view(), name='blog_list'),
    # path('<slug:slug>/', Home.as_view(), name='blog_detail'),
]
