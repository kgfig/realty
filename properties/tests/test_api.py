import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from properties.models import Location, Project, RealProperty, Unit

class ProjectViewsTest(TestCase):

    def test_resolves_url_to_detail_view(self):
        location = Location(municipality="Silang", province="Cavite")
        location.save()
        
        project = Project(name="Coral Grove", location=location)
        project.save()

        response = self.client.get(reverse('projects:detail', kwargs={'pk': project.id}))
        self.assertEqual(response.status_code, 200)
        

    def test_resolves_url_to_list_view(self):
        response = self.client.get(reverse('projects:list'))
        self.assertEqual(response.status_code, 200)
        
