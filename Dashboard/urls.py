from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerDashboardViewSet, JobSeekerDashboardViewSet

router = DefaultRouter()
router.register('employer-dashboard', EmployerDashboardViewSet, basename='employer-dashboard')
router.register('jobseeker-dashboard', JobSeekerDashboardViewSet, basename='jobseeker-dashboard')

urlpatterns = [
    path('', include(router.urls)),
]
