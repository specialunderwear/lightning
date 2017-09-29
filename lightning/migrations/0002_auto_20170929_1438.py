# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-09-29 14:38
from __future__ import unicode_literals

import dedupebackend.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dedupebackend', '0001_initial'),
        ('lightning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='henkendorp',
            name='uniquefile',
            field=dedupebackend.fields.UniqueImageField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dedupebackend.UniqueFile'),
        ),
        migrations.AddField(
            model_name='henkendorp',
            name='uniqueimage',
            field=dedupebackend.fields.UniqueImageField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='dedupebackend.UniqueFile'),
        ),
    ]
