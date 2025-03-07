from django import forms
from .models import Barber, Service, Appointment, Reviews
from rest_framework import serializers

class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber
        fields = ['name', 'bio', 'rating']
    
    def clean(self):
        cleaned_data = super().clean()
        print(f"Cleaned Data: {cleaned_data}")
        return cleaned_data


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['barber', 'name', 'duration', 'description', 'price']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'barber']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'barber': forms.Select(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['barber', 'user', 'rating', 'comment']