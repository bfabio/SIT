# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-28 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190116_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='inspire_default_language',
            field=models.CharField(blank=True, default='ita', help_text='3 letter code of the default language (see http://inspire.ec.europa.eu/schemas/common/1.0/enums/enum_eng.xsd, simpleType euLanguageISO6392B)', max_length=255, null=True, verbose_name='inspire_default_language'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='inspire_enabled',
            field=models.BooleanField(default=False, help_text='whether to enable the INSPIRE extension', verbose_name='inspire_enabled'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='inspire_gemet_keywords',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Addresses', 'Addresses'), ('Administrative units', 'Administrative units'), ('Agricultural and aquaculture facilities', 'Agricultural and aquaculture facilities'), ('Area management/restriction/regulation zones and reporting units', 'Area management/restriction/regulation zones and reporting units'), ('Atmospheric conditions', 'Atmospheric conditions'), ('Bio-geographical regions', 'Bio-geographical regions'), ('Buildings', 'Buildings'), ('Cadastral parcels', 'Cadastral parcels'), ('Coordinate reference systems', 'Coordinate reference systems'), ('Elevation', 'Elevation'), ('Energy resources', 'Energy resources'), ('Environmental monitoring facilities', 'Environmental monitoring facilities'), ('Geographical grid systems', 'Geographical grid systems'), ('Geographical names', 'Geographical names'), ('Geology', 'Geology'), ('Habitats and biotopes', 'Habitats and biotopes'), ('Human health and safety', 'Human health and safety'), ('Hydrography', 'Hydrography'), ('Land cover', 'Land cover'), ('Land use', 'Land use'), ('Meteorological geographical features', 'Meteorological geographical features'), ('Mineral resources', 'Mineral resources'), ('Natural risk zones', 'Natural risk zones'), ('Oceanographic geographical features', 'Oceanographic geographical features'), ('Orthoimagery', 'Orthoimagery'), ('Population distribution \u2014 demography', 'Population distribution \u2014 demography'), ('Production and industrial facilities', 'Production and industrial facilities'), ('Protected sites', 'Protected sites'), ('Sea regions', 'Sea regions'), ('Soil', 'Soil'), ('Species distribution', 'Species distribution'), ('Statistical units', 'Statistical units'), ('Transport networks', 'Transport networks'), ('Utility and governmental services', 'Utility and governmental services')], help_text='a comma-seperated keyword list of GEMET INSPIRE theme keywords about the service (see http://inspire.ec.europa.eu/schemas/common/1.0/enums/enum_eng.xsd, complexType inspireTheme_eng)', max_length=1024, null=True, verbose_name='inspire_gemet_keywords'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='inspire_languages_supported',
            field=models.CharField(blank=True, default='ita', help_text='list of comma separated 3 letter codes of supported languages (see http://inspire.ec.europa.eu/schemas/common/1.0/enums/enum_eng.xsd, simpleType euLanguageISO6392B)', max_length=255, null=True, verbose_name='inspire_languages_supported'),
        ),
        migrations.AlterField(
            model_name='record',
            name='links',
            field=models.CharField(blank=True, help_text='Maps to pycsw:Links', max_length=1024, null=True),
        ),
    ]
