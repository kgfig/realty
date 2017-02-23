from django.core.urlresolvers import reverse
from django.test import TestCase

from properties.models import Location, Project, RealProperty, Unit

# TODO: read on designing APIs
# TODO: read Queryset.get_or_create()

class LocationsAPITestCase(TestCase):

    def setUp(self):
        silang = Location(municipality='Silang', province='Cavite')
        dasma = Location(municipality='Dasmarinas', province='Cavite')
        
        silang.save()
        dasma.save()
        
        self.list_url = reverse('projects:locations_api')
        self.detail_url = reverse('projects:locations_api', kwargs={'pk': silang.id})

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, 'Silang')
        self.assertContains(response, 'Dasmarinas')
        self.assertContains(response, 'Cavite')
        
    def test_detail(self):
        response = self.client.get(self.detail_url, format='json')
        content = {
            'id': 1,
            'municipality': 'Silang',
            'province': 'Cavite',
            'projects': []
        }
        self.assertEqual(response.data, content)

class ProjectsAPITestCase(TestCase):

    def setUp(self):
        silang = Location(municipality='Silang', province='Cavite')
        dasma = Location(municipality='Dasmarinas', province='Cavite')
        silang.save()
        dasma.save()

        grove = Project(name='Coral Grove', location=silang)
        woods = Project(name='Lush Woods', location=dasma)
        grove.save()
        woods.save()

        self.list_url = reverse('projects:projects_api')
        self.detail_url = reverse('projects:projects_api', kwargs={'pk': grove.id})

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, 'Coral Grove')
        self.assertContains(response, 'Silang')
        self.assertContains(response, 'Lush Woods')
        self.assertContains(response, 'Dasmarinas')
        self.assertContains(response, 'Cavite')
        
    def test_detail(self):
        response = self.client.get(self.detail_url)
        content = {
            'id': 1,
            'name': 'Coral Grove',
            'location': {
                    'id': 1,
                    'municipality': 'Silang',
                    'province': 'Cavite'
            },
            'real_properties': []
        }
        self.assertEqual(response.data, content)        

class PropertyAPITestCase(TestCase):

    def setUp(self):
        silang = Location(municipality='Silang', province='Cavite')
        silang.save()
        grove = Project(name='Coral Grove', location=silang)
        grove.save()

        magnolia = RealProperty(
            description='Magnolia (3B Bungalow with Loft)',
            category=RealProperty.CATEGORIES.house_and_lot,
            lowest_price=1900000,
            highest_price=2400000,
            lot_area=90,
            project=grove
        )
        magnolia.save()

        vanilla = RealProperty(
            description='Vanilla (3B 2-storey house and lot)',
            category=RealProperty.CATEGORIES.house_and_lot,
            lowest_price=2100000,
            highest_price=2500000,
            lot_area=80,
            project=grove
        )
        vanilla.save()

        magnolia_unit1 = Unit(status=Unit.STATUS.reserved, real_property=magnolia)
        magnolia_unit1.save()
        
        self.list_url = reverse('projects:properties_api')
        self.detail_url = reverse('projects:properties_api', kwargs={'pk': magnolia.id})

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, 'Magnolia')
        self.assertContains(response, '3B Bungalow with Loft')
        self.assertContains(response, 'Vanilla')
        self.assertContains(response,'3B 2-storey house and lot')

    def test_detail(self):
        response = self.client.get(self.detail_url)
        content = {
            'id': 1,
            'description': 'Magnolia (3B Bungalow with Loft)',
            'category': RealProperty.CATEGORIES.house_and_lot,
            'lowest_price': 1900000,
            'highest_price': 2400000,
            'lot_area': 90,
            'units': [
                 {
                     'id': 1,
                     'status': Unit.STATUS.reserved
                 }   
            ]
        }
        self.assertEqual(response.data, content)
