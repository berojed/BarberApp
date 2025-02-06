from rest_framework import viewsets, permissions
from .models import Appointment,Barber
from .serializers import AppointmentSerializer,BarberSerializer
from django.utils import timezone

class AppointmentViewSet(viewsets.ModelViewSet):

    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created_at=timezone.now())


