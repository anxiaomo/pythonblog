# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-09-06 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='标题')),
                ('body', models.TextField(verbose_name='内容')),
            ],
            options={
                'indexes': [],
            },
        ),
    ]
