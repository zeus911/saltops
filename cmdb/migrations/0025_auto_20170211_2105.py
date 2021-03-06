# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0024_hostip_ip_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='minion_status',
            field=models.IntegerField(choices=[(0, '未启动'), (1, '运行中'), (2, '待接受'), (3, '已拒绝'), (4, '已禁止')], default=0, verbose_name='Minion状态'),
        ),
    ]
