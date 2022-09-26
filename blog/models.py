from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager

# from markdownx.models import MarkdownxField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250, unique_for_date='publish')
    slug = models.CharField(_("Slug"), max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField()
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
    slug = models.SlugField(max_length=300, unique_for_date='date')
    url = models.URLField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    # rp_body = models.TextField()

    def __str__(self):
        return self.rp_title

    class Meta:
        ordering = ('rp_title',)

    def get_absolute_url(self):
        return reverse('report:report_detail', args=[self.slug])


#
#
# class Gallery(models.Model):
#     img_w = models.PositiveIntegerField(default=250)
#     img_h = models.PositiveIntegerField(default=413)
#     photo = models.ImageField(upload_to=None, height_field='img_h', width_field='img_w')

class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    news_title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250, unique_for_date='nw_publish', unique=True, null=True)
    slug = models.SlugField(max_length=300, unique_for_date='nw_publish')
    news_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')
    news_body = RichTextField()
    # image_header = models.ImageField(null=True, blank=True)

    image_header = models.ImageField(upload_to='featured_image/%Y/%m/%d/', null=True, blank=True)  # this

    nw_publish = models.DateTimeField(default=timezone.now)
    nw_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    news_tags = TaggableManager()

    class Meta:
        ordering = ('nw_publish',)

    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.slug])


class Member(models.Model):
    mm_name = models.CharField(max_length=500)
    # date = models.DateTimeField(default=timezone.now)
    mm_position = models.CharField(max_length=400)
    mm_image = models.ImageField(unique=True)

    # rp_body = models.TextField()

    def __str__(self):
        return self.mm_name

    class Meta:
        ordering = ('mm_name',)

    # def get_absolute_url(self):
    #     return reverse('report:report_detail', args=[self.mm_name])


class Project(models.Model):
    pr_title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=300, unique_for_date='date')
    url = models.URLField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pr_title

    class Meta:
        ordering = ('pr_title',)

    def get_absolute_url(self):
        return reverse('project:project_detail', args=[self.slug])
