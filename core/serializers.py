from rest_framework import serializers
from .models import *


class ServiceStepSerialize(serializers.ModelSerializer):
    class Meta:
        model = ServiceStep
        fields = ('id', 'title', 'text')


class ServiceSerializer(serializers.ModelSerializer):
    # steps = ServiceStepSerialize(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ("id", "name", "description", "miniature", "expiry_date", "steps")


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("id", "project_id", "text", "image")


class ProjectSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ("id", "name", "text", "miniature", "link", "service_id", "task", "about_company", "gallery")

    # def create(self, validated_data):
    #     gallery_data = validated_data.pop('gallery')
    #     project = Project.objects.create(**validated_data)
    #     for gallery_data in gallery_data:
    #         Project.objects.create(project=project, **gallery_data)
    #     return project
