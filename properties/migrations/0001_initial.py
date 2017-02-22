# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('municipality', models.CharField(max_length=64)),
                ('province', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('location', models.ForeignKey(to='properties.Location', on_delete=django.db.models.deletion.DO_NOTHING)),
            ],
        ),
        migrations.CreateModel(
            name='RealProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=128, blank=True)),
                ('category', models.IntegerField(default=1, choices=[(1, 'House and Lot'), (2, 'Lot Only')])),
                ('lowest_price', models.PositiveIntegerField()),
                ('highest_price', models.PositiveIntegerField()),
                ('lot_area', models.PositiveIntegerField()),
                ('project', models.ForeignKey(to='properties.Project')),
            ],
        ),
    ]
