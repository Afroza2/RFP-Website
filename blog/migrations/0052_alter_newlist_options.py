# Generated by Django 3.2.7 on 2023-12-22 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0051_auto_20231222_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newlist',
            options={'ordering': ['position', 'mem_name']},
        ),
    ]
