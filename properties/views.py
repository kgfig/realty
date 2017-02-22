from django.views.generic import ListView, DetailView, UpdateView

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectUpdateView(UpdateView):
    model = Project

    # Redirect to this objects' detail view
    def get_success_url(self):
        return reverse('projects:detail', kwargs={'pk': self.object.pk})

class ProjectListAPI(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPI(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
