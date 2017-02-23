from django.views.generic import ListView, DetailView, UpdateView

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Project, Location, RealProperty
from .serializers import ProjectSerializer, LocationSerializer, RealPropertySerializer

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectUpdateView(UpdateView):
    model = Project

    # Redirect to this objects' detail view
    def get_success_url(self):
        return reverse('projects:detail', kwargs={'pk': self.object.pk})

class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationRetrieveAPIView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class PropertyListAPIView(ListAPIView):
    queryset = RealProperty.objects.all()
    serializer_class = RealPropertySerializer

class PropertyRetrieveAPIView(RetrieveAPIView):
    queryset = RealProperty.objects.all()
    serializer_class = RealPropertySerializer
