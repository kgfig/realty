from django.db import models
from django.utils.translation import gettext as _

from model_utils.fields import MonitorField
from model_utils import Choices

class Location(models.Model):
    municipality = models.CharField(max_length = 64)
    province = models.CharField(max_length = 64)

    def __str__(self):
        return '%s, %s' % (self.municipality, self.province)

class Project(models.Model):
    name = models.CharField(max_length = 64)
    location = models.ForeignKey(Location, related_name='projects', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class RealProperty(models.Model):
    CATEGORIES = Choices(
            ('house_and_lot', _('House and Lot')),
            ('lot_only', _('Lot Only'))
        )
    name = models.CharField(max_length = 64, blank=True)
    description = models.CharField(max_length = 128, blank=True)
    category = models.CharField(max_length=32, choices=CATEGORIES, default=CATEGORIES.house_and_lot)
    project = models.ForeignKey(Project, related_name='real_properties', on_delete=models.CASCADE)
    lowest_price = models.PositiveIntegerField()
    highest_price = models.PositiveIntegerField()
    lot_area = models.PositiveIntegerField()

    def __str__(self):
        return '%s (%s) - %d sqm for PHP%d' %(self.description, RealProperty.CATEGORIES[self.category], self.lot_area, self.lowest_price)

class Unit(models.Model):
    STATUS = Choices(
        ('available', _('Available')),
        ('reserved', _('Reserved')),
        ('sold', _('Sold'))
        )
    
    real_property = models.ForeignKey(RealProperty, related_name='units', on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=STATUS, default=STATUS.available)
    last_updated = MonitorField(monitor='status')

    def __str__(self):
        return '%s is %s as of %s' % (self.real_property.description, Unit.STATUS[self.status], self.last_updated.strftime("%m/%d/%Y"))

    
    
    
    
