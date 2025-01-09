
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.JobSeekersViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.JobSeekersRegistrationApiView.as_view(), name='register'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('login/', views.JobSeekersLoginApiView.as_view(), name='login'),
    path('logout/', views.JobSeekersLogoutView.as_view(), name='logout'),
]