# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='user_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='login_app.Users'),
        ),
    ]
