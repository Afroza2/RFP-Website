# Generated by Django 3.2.7 on 2022-09-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220903_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_header',
            field=models.ImageField(unique=True, upload_to=''),
        ),
    ]
