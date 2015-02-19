# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='書籍名', max_length=255)),
                ('publisher', models.CharField(verbose_name='出版社', max_length=255, blank=True)),
                ('page', models.IntegerField(verbose_name='#page', default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='comment', blank=True)),
                ('book', models.ForeignKey(to='cms.Book', verbose_name='書籍', related_name='impressions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
