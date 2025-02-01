from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register('applications', ApplicationViewSet, basename='application')

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
