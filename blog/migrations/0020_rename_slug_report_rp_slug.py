# Generated by Django 3.2.7 on 2022-09-23 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='slug',
            new_name='rp_slug',
        ),
    ]
