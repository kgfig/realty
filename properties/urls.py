from django.conf.urls import include, url

from .views import ProjectListView, ProjectDetailView, ProjectUpdateView
from .views import ProjectListAPIView, ProjectRetrieveAPIView, LocationListAPIView, LocationRetrieveAPIView, PropertyListAPIView, PropertyRetrieveAPIView

urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='detail'),
    url(r'^api/projects/$', ProjectListAPIView.as_view(), name='projects_api'),
    url(r'^api/projects/(?P<pk>\d+)/$', ProjectRetrieveAPIView.as_view(), name='projects_api'),
    url(r'^api/locations/$', LocationListAPIView.as_view(), name='locations_api'),
    url(r'^api/locations/(?P<pk>\d)/$', LocationRetrieveAPIView.as_view(), name='locations_api'),
    url(r'^api/properties/$', PropertyListAPIView.as_view(), name='properties_api'),
    url(r'^api/properties/(?P<pk>\d+)/$', PropertyRetrieveAPIView.as_view(), name='properties_api'),
]
