# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-14 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0002_articles_correlate_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='correlate_articles',
            field=models.ManyToManyField(blank=True, related_name='_articles_correlate_articles_+', to='law.Articles', verbose_name='Correlate articles'),
        ),
    ]
