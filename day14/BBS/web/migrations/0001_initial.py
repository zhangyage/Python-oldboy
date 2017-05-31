# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='web.Admin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('summary', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('favor_count', models.IntegerField(default=0)),
                ('replay_count', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('new', models.ForeignKey(to='web.News')),
                ('user', models.ForeignKey(to='web.Admin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(to='web.NewType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(to='web.Admin'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='admin',
            name='user_type',
            field=models.ForeignKey(to='web.UserType'),
            preserve_default=True,
        ),
    ]
