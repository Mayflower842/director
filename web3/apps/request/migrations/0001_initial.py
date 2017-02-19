# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-19 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('teacher_approval', models.BooleanField(default=False)),
                ('admin_approval', models.BooleanField(default=False)),
                ('activity', models.CharField(max_length=32)),
                ('extra_information', models.TextField(blank=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_requests', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_sites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
