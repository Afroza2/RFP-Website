# RFP_website/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('projects/', include('blog.urls', namespace='project')),
    path('photo-gallery/', include('blog.urls', namespace='gallery')),
    path('video-gallery/', include('blog.urls', namespace='video')),
    path('reports/', include('blog.urls', namespace='report')),
    path('members/', include('blog.urls', namespace='members')),
    path('news/', include('blog.urls', namespace='news')),
    path('blognews/', include('blog.urls', namespace='blognews')),
    path('contact/', include('blog.urls', namespace='contact')),
    path('new-committee/', include('blog.urls', namespace='new_committee')),
    path('former-committee/', include('blog.urls', namespace='former_committee')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
