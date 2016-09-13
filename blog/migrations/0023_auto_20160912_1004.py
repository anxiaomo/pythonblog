# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-12 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20160909_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default=1, max_length=300, verbose_name='摘要'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='des',
            field=models.CharField(max_length=100, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to='./photo1', verbose_name='图片'),
        ),
    ]
