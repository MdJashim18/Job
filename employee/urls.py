from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import EmployeeViewset, EmployeeRegistrationApiView, EmployeeLoginApiView, EmployeeLogoutView, activate,VerifyTokenAPIView

router = DefaultRouter()
router.register('list', EmployeeViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', EmployeeRegistrationApiView.as_view(), name='register'),
    path('active/<uid64>/<token>/', activate, name='activate'),
    path('login/', EmployeeLoginApiView.as_view(), name='login'),
    path('logout/', EmployeeLogoutView.as_view(), name='logout'),
    path('verify_token/',VerifyTokenAPIView.as_view(), name='verify_token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
