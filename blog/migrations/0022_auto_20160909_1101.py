# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-09 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20160908_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(blank=True, verbose_name='网站'),
        ),
        migrations.AlterField(
            model_name='classification',
            name='name',
            field=models.CharField(max_length=20, verbose_name='文章分类'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=20, verbose_name='标签'),
        ),
    ]
