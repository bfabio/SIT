# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-28 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_merge_20190128_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='rndt_codice_ipa',
            field=models.CharField(blank=True, help_text='RNDT: codice iPA amministrazione, parte di fileIdentifier', max_length=32, null=True, verbose_name='RNDT codice iPA amministrazione'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='rndt_enabled',
            field=models.BooleanField(default=False, help_text='whether to enable the RNDT extension', verbose_name='RNDT enabled'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='rndt_file_identifier',
            field=models.CharField(blank=True, help_text='RNDT: fileIdentifier', max_length=128, null=True, verbose_name='RNDT identificatore del file'),
        ),
    ]
