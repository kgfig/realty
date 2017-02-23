from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver

from properties.models import Project, Location, RealProperty, Unit

class ProjectsTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls)
