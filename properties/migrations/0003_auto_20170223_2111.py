# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='realproperty',
            name='name',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.ForeignKey(related_name='projects', to='properties.Location', on_delete=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AlterField(
            model_name='realproperty',
            name='category',
            field=models.CharField(max_length=32, choices=[('house_and_lot', 'House and Lot'), ('lot_only', 'Lot Only')], default='house_and_lot'),
        ),
        migrations.AlterField(
            model_name='realproperty',
            name='project',
            field=models.ForeignKey(to='properties.Project', related_name='real_properties'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='real_property',
            field=models.ForeignKey(to='properties.RealProperty', related_name='units'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.IntegerField(choices=[('available', 'Available'), ('reserved', 'Reserved'), ('sold', 'Sold')], default='available'),
        ),
    ]
