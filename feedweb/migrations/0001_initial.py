# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='pub_date')),
            ],
        ),
        migrations.CreateModel(
            name='FeedCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FeedLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_language_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=250)),
                ('section_body', models.TextField(max_length=5000)),
                ('section_video_url', models.URLField(blank=True, max_length=2000)),
                ('section_image', models.ImageField(upload_to='uploads/%Y/%m/%d/images')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedweb.Feed')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='feed_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedweb.FeedCategory'),
        ),
        migrations.AddField(
            model_name='feed',
            name='feed_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedweb.FeedLanguage'),
        ),
    ]