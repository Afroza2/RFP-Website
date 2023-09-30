# Generated by Django 3.2.7 on 2023-04-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20230428_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_img_h',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_img_w',
        ),
        migrations.AlterField(
            model_name='news',
            name='image_header',
            field=models.ImageField(blank=True, height_field='img_h', null=True, upload_to='featured_image/%Y/%m/%d/', width_field='img_w'),
        ),
    ]
