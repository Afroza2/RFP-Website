from django.contrib import admin

# Register your models here.

from .models import Post, Report
from markdownx.admin import MarkdownxModelAdmin


# Report, Gallery


#
# admin.site.register(Post)


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')


admin.site.register(Post, MarkdownxModelAdmin)


#
# @admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('rp_title', 'url', 'date')
    list_filter = ('rp_title', 'date')
    search_fields = ('rp_title', 'body')
    prepopulated_fields = {'slug': ('rp_title',)}
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    ordering = ('rp_title', 'date')


admin.site.register(Report, ReportAdmin)
#
#
# admin.site.register(Gallery)
# # class GalleryAdmin(admin.ModelAdmin):
