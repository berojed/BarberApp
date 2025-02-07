from rest_framework import serializers
from .models import Barber,Appointment

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    barber = serializers.StringRelatedField()
    
    class Meta:
        model = Appointment
        fields = ['id', 'user', 'barber', 'date', 'time', 'created_at', 'is_confirmed']
        read_only_fields = ['id', 'created_at', 'user'] 


