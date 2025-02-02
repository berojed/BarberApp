from django import forms
from .models import Barber, Service, Appointment, Reviews
from rest_framework import serializers

class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber
        fields = ['name', 'bio', 'rating']
    
    def clean(self):
        cleaned_data = super().clean()
        print(f"Cleaned Data: {cleaned_data}")  # Ovo će ispisati podatke u konzolu
        return cleaned_data


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['barber', 'name', 'duration', 'description', 'price']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user', 'barber', 'time', 'date', 'created_at', 'is_confirmed']
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['barber', 'user', 'rating', 'comment']