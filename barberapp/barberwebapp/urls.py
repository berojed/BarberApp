from django.urls import path, include
from . import views
from .views import (
    BarberListView, BarberDetailView,
    ServiceListView, ServiceDetailView,
    AppointmentListView, AppointmentDetailView,
    ReviewsListView, ReviewsDetailView,
    create_barber, update_barber, BarberDeleteView, 
    create_service, update_service, ServiceDeleteView, 
    create_appointment, update_appointment, AppointmentDeleteView, 
    create_review, update_review, ReviewDeleteView,
)
from . import urls_api

app_name = 'barberwebapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
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
    path('barbers/create/', create_barber, name='create_barber'), 
    path('barbers/<int:pk>/update/', update_barber, name='update_barber'), 
    path('barbers/<int:pk>/delete/', BarberDeleteView.as_view(), name='delete_barber'), 
    path('services/create/', create_service, name='create_service'), 
    path('services/<int:pk>/update/', update_service, name='update_service'), 
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='delete_service'), 
    path('appointments/create/', create_appointment, name='create_appointment'), 
    path('appointments/<int:pk>/update/', update_appointment, name='update_appointment'), 
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='delete_appointment'), 
    path('reviews/create/', create_review, name='create_review'), 
    path('reviews/<int:pk>/update/', update_review, name='update_review'), 
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete_review'),
]