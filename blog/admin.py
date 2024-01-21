from django.contrib import admin

# Register your models here.

from .models import Post, Report, News, Member, Project, Gallery, Video, FList, NewList


# from markdownx.admin import MarkdownxModelAdmin


# Report, Gallery


#
# admin.site.register(Post)


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')


admin.site.register(Post, PostAdmin)


#
# @admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('rp_title',  'date')
    list_filter = ('rp_title', 'date')
    search_fields = ('rp_title', 'date')
    # prepopulated_fields = {'slug': ('rp_title',)}
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    ordering = ('rp_title', 'date')


admin.site.register(Report, ReportAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('vid_title', 'url')


admin.site.register(Video, VideoAdmin)


#
#
# admin.site.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('p_caption', 'p_date')
    list_filter = ('p_caption', 'p_date')
    search_fields = ('p_caption', 'p_date')
    prepopulated_fields = {'p_slug': ('p_caption',)}


admin.site.register(Gallery, GalleryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'slug', 'news_author', 'nw_publish', 'nw_status')
    list_filter = ('nw_status', 'nw_publish', 'news_author')
    search_fields = ('news_title', 'news_body')
    prepopulated_fields = {'slug': ('news_title',)}
    ordering = ('nw_publish', 'news_title')


admin.site.register(News, NewsAdmin)

class FCAdmin(admin.ModelAdmin):
    list_display = ('f_list', 'date')
    list_filter = ('f_list', 'date')
    search_fields = ('f_list',)
    # prepopulated_fields = {'slug': ('f_l',)}
    ordering = ('f_list', 'date')


admin.site.register(FList, FCAdmin)

class NCAdmin(admin.ModelAdmin):
    list_display = ('mem_name', 'position', 'faith')
    list_filter = ('mem_name', 'position')
    search_fields = ('mem_name',)
    ordering = ('mem_name', 'position')


admin.site.register(NewList, NCAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('mm_name', 'mm_position')
    list_filter = ('mm_name', 'mm_position')
    search_fields = ('mm_name', 'mm_position')
    # prepopulated_fields = {'slug': ('news_title',)}
    ordering = ('mm_name', 'mm_position')


admin.site.register(Member, MemberAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pr_title', 'url', 'date')
    list_filter = ('pr_title', 'date')
    search_fields = ('pr_title',)
    prepopulated_fields = {'slug': ('pr_title',)}
    ordering = ('pr_title', 'date')


admin.site.register(Project, ProjectAdmin)
