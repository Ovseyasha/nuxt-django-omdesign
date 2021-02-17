from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class ServiceStepViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceStepSerialize
    queryset = ServiceStep.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()

    # def get_queryset(self):
    #     queryset = Gallery.objects.all()
    #     query_param = self.request.query_params.get('project_id', None)
    #     print(self.request.query_params.getlist())
    #
    #     if query_param is not None:
    #         queryset = Gallery.objects.filter(project_id=query_param)
    #
    #     return queryset
