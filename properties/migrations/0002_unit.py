# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('status', models.IntegerField(choices=[(1, 'Available'), (2, 'Reserved'), (3, 'Sold')], default=1)),
                ('last_updated', model_utils.fields.MonitorField(monitor='status', default=django.utils.timezone.now)),
                ('real_property', models.ForeignKey(to='properties.RealProperty')),
            ],
        ),
    ]
