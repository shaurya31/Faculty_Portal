# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0009_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='faculty/Photos/2.jpg', null=True, upload_to='faculty/Photos'),
        ),
    ]