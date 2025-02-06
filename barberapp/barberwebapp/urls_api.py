app_name = 'barberapp'  # ili neki drugi naziv koji želite koristiti

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AppointmentViewSet  

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('', include(router.urls)),
]