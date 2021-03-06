# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_usergroup_ctime'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='uptime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '普普通用户')], default=1),
        ),
    ]
