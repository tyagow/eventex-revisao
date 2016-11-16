# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-12 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('photo', models.URLField(verbose_name='foto')),
                ('website', models.URLField(blank=True, verbose_name='website')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
        ),
    ]
