# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_date', models.DateField(verbose_name='Created Date', blank=True, null=True)),
                ('name', models.CharField(verbose_name='Contact name', max_length=50)),
                ('email', models.EmailField(verbose_name='Contact Email', blank=True, null=True, max_length=50)),
                ('phone', models.CharField(verbose_name='Contact Number', blank=True, null=True, max_length=15)),
                ('message', models.TextField(verbose_name='Detailed message', blank=True, null=True, max_length=500)),
                ('attended', models.BooleanField(verbose_name='Attended to Contact Request', default=False)),
            ],
        ),
    ]
