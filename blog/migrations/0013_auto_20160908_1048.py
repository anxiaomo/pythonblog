# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-08 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160908_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to='../pythonblog/public/temp'),
        ),
    ]
