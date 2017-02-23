from django.test import TestCase

from properties.models import Location, Project, RealProperty, Unit

class LocationTestCase(TestCase):

    def test_can_save_and_get_location(self):
        location = Location()
        location.municipality = "Silang"
        location.province = "Cavite"
        location.save()

        saved_location = Location.objects.first()
        self.assertEqual(saved_location, location)
        self.assertEqual(saved_location.__str__(), "Silang, Cavite")

class ProjectTestCase(TestCase):

    def test_can_save_and_get_project(self):
        location = Location()
        location.municipality = "Silang"
        location.province = "Cavite"
        location.save()
        
        project = Project(name="Coral Grove")
        project.location = location
        project.save()

        saved_project = Project.objects.first()
        self.assertEqual(saved_project.location, location)

class RealPropertyTestCase(TestCase):

    def test_can_save_and_get_real_property(self):
        location = Location()
        location.municipality = "Silang"
        location.province = "Cavite"
        location.save()
        
        project = Project(name="Coral Grove")
        project.location = location
        project.save()
        
        real_property = RealProperty()
        real_property.description = "3B Bungalow with Loft"
        real_property.category =  RealProperty.CATEGORIES.house_and_lot
        real_property.project = project
        real_property.lowest_price = 1900000
        real_property.highest_price = 2400000
        real_property.lot_area = 90
        real_property.save()

        saved_property = RealProperty.objects.first()
        print(saved_property)
        self.assertEqual(saved_property, real_property)

class UnitTestCase(TestCase):

    def test_can_save_and_get_unit(self):
        location = Location()
        location.municipality = "Silang"
        location.province = "Cavite"
        location.save()
        
        project = Project(name="Coral Grove")
        project.location = location
        project.save()
        
        hlProperty = RealProperty()
        hlProperty.description = "3B Bungalow with Loft"
        hlProperty.category =  RealProperty.CATEGORIES.house_and_lot
        hlProperty.project = project
        hlProperty.lowest_price = 1900000
        hlProperty.highest_price = 2400000
        hlProperty.lot_area = 90
        hlProperty.save()

        unit = Unit(real_property=hlProperty, status=Unit.STATUS.reserved)
        unit.save()

        other_unit = Unit(real_property = hlProperty, status=Unit.STATUS.available)
        other_unit.save()

        saved_units_count = Unit.objects.count()
        reserved_unit = Unit.objects.get(status=Unit.STATUS.reserved)
        available_unit = Unit.objects.get(status=Unit.STATUS.available)
        print(reserved_unit)
        print(other_unit)
        self.assertEqual(saved_units_count, 2)
        self.assertEqual(reserved_unit.id, unit.id)
        self.assertEqual(available_unit.id, other_unit.id)
        
