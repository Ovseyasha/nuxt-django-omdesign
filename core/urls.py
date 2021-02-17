from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'service', ServiceViewSet)
router.register(r'service-steps', ServiceStepViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'gallery', GalleryViewSet)

urlpatterns = [
    path("", include(router.urls))
]
