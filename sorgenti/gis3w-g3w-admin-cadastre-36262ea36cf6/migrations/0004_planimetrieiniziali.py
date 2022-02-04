# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0003_auto_20161118_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanimetrieIniziali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice_comune', models.CharField(max_length=4)),
                ('codice_generico', models.IntegerField(blank=True, null=True)),
                ('foglio', models.CharField(max_length=4)),
                ('numero', models.CharField(max_length=5)),
                ('subalterno', models.CharField(max_length=4, null=True)),
                ('nome_file', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'planimetrie_iniziali',
                'verbose_name': 'Planimetria iniziale',
                'verbose_name_plural': 'Planimetrie iniziali',
            },
        ),
    ]
