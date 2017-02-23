from django.test import TestCase

from properties.models import Location, Project, RealProperty, Unit

class LocationTestCase(TestCase):

    def setUp(self):
        self.location = Location(municipality='Silang', province='Cavite')
        self.location.save()

    def test_can_save_and_get_location(self):
        saved_location = Location.objects.first()
        self.assertEqual(saved_location, self.location)

class ProjectTestCase(TestCase):

    def setUp(self):
        location = Location(municipality='Silang', province='Cavite')
        location.save()
        
        self.project = Project(name="Coral Grove", location=location)
        self.project.save()

    def test_can_save_and_get_project(self):
        saved_project = Project.objects.first()
        self.assertEqual(saved_project, self.project)

class RealPropertyTestCase(TestCase):

    def setUp(self):
        location = Location(municipality='Silang', province='Cavite')
        location.save()
        
        project = Project(name="Coral Grove", location=location)
        project.save()
        
        self.hl_property = RealProperty(
            name = 'Magnolia',
            description='3B Bungalow with Loft',
            category=RealProperty.CATEGORIES.house_and_lot,
            project=project,
            lowest_price=1900000,
            highest_price=2400000,
            lot_area=90
        )
        self.hl_property.save()


    def test_can_save_and_get_real_property(self):
        saved_property = RealProperty.objects.first()
        self.assertEqual(saved_property, self.hl_property)

class UnitTestCase(TestCase):

    def setUp(self):
        location = Location(municipality='Silang', province='Cavite')
        location.save()
        
        project = Project(name="Coral Grove", location=location)
        project.save()
        
        hl_property = RealProperty(
            name = 'Magnolia',
            description='3B Bungalow with Loft',
            category=RealProperty.CATEGORIES.house_and_lot,
            project=project,
            lowest_price=1900000,
            highest_price=2400000,
            lot_area=90
        )
        hl_property.save()

        self.unit = Unit(real_property=hl_property, status=Unit.STATUS.reserved)
        self.unit.save()

        self.other_unit = Unit(real_property=hl_property, status=Unit.STATUS.available)
        self.other_unit.save()

    def test_can_save_and_get_unit(self):
        saved_units_count = Unit.objects.count()
        reserved_unit = Unit.objects.get(status=Unit.STATUS.reserved)
        available_unit = Unit.objects.get(status=Unit.STATUS.available)
        
        self.assertEqual(saved_units_count, 2)
        self.assertEqual(reserved_unit.id, self.unit.id)
        self.assertEqual(available_unit.id, self.other_unit.id)
        
