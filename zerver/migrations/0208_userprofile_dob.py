# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-04 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0207_multiuseinvite_invited_as'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
