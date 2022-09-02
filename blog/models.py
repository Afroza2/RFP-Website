from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from markdownx.models import MarkdownxField


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = MarkdownxField()
    # image_header = models.ImageField(unique=True, default=timezone.now)
    publish = models.DateTimeField(default=timezone.now)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:details', args=[self.slug])


#
# class ImageList(models.Model):
#     body_image = models.ImageField(null=True, blank=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#
#
class Report(models.Model):
    rp_title = models.CharField(max_length=500)
    slug = models.CharField(_("Slug"), max_length=200)
    url = models.URLField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    # rp_body = models.TextField()

    def __str__(self):
        return self.rp_title

    class Meta:
        ordering = ('date',)

    def get_absolute_url(self):
        return reverse('report:report_detail', args=[self.slug])
#
#
# class Gallery(models.Model):
#     img_w = models.PositiveIntegerField(default=250)
#     img_h = models.PositiveIntegerField(default=413)
#     photo = models.ImageField(upload_to=None, height_field='img_h', width_field='img_w')
