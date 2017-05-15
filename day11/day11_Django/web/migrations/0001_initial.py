# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Gender', models.BooleanField(default=False)),
                ('Age', models.IntegerField(default=22)),
                ('memo', models.TextField(default=b'zhangyage')),
                ('CreateDate', models.DateTimeField(default=b'2017-05-15 11:30:00')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
