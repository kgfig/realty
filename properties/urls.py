from django.conf.urls import include, url

from .views import ProjectListView, ProjectDetailView, ProjectUpdateView

urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='detail'),
]
