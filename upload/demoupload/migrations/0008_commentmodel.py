# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoupload', '0007_likemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=555)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoupload.PostModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoupload.UserModel')),
            ],
        ),
    ]
