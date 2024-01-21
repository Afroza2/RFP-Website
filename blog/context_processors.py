# blog/context_processors.py
from taggit.models import Tag
from blog.models import Report
from django.db.models import Count
from django.db.models.functions import ExtractYear
from datetime import datetime

def site_info(request):
    # Get all tags
    all_tags = Tag.objects.all()

    # Get year-wise archive list
    year_archive = Report.objects.annotate(year=ExtractYear('date')).values('year').annotate(count=Count('id'))

    return {
        'all_tags': all_tags,
        'year_archive': year_archive,
    }
