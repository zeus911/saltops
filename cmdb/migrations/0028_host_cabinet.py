# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 03:43
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0027_auto_20170217_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='cabinet',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='rack', chained_model_field='rack', null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Cabinet'),
        ),
    ]
