# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20170223_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='realproperty',
            name='floor_area',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('reserved', 'Reserved'), ('sold', 'Sold')], max_length=16, default='available'),
        ),
    ]
