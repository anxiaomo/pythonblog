# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-08 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160908_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to='./public/temp'),
        ),
    ]
