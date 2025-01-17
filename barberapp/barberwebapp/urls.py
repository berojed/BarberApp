from django.urls import path, include
from . import views
from .views import (
    BarberListView, BarberDetailView,
    ServiceListView, ServiceDetailView,
    AppointmentListView, AppointmentDetailView,
    ReviewsListView, ReviewsDetailView,
)
from . import urls_api

app_name = 'barberwebapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('barbers/', BarberListView.as_view(), name='barber_list'),
    path('barbers/<int:pk>/', BarberDetailView.as_view(), name='barber_detail'),
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('reviews/', ReviewsListView.as_view(), name='reviews_list'),
    path('reviews/<int:pk>/', ReviewsDetailView.as_view(), name='reviews_detail'),
    path('api/', include(urls_api)),
]