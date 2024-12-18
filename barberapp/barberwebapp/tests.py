from django.test import TestCase
from django.urls import reverse
from .models import Barber, Service, Appointment, Reviews, User
from datetime import datetime, timedelta
from django.utils import timezone
from django.template.defaultfilters import time as time_filter

class BarberWebAppTests(TestCase):

    def setUp(self):
        # Kreiranje korisnika
        self.user = User.objects.create_user(username='testuser', password='testpassword', phone_number=123456789)

        
        self.barber = Barber.objects.create(
            name='Test Barber',
            bio='Iskusni profesionalac.',
            rating=5
        )

        
        self.service = Service.objects.create(
            barber=self.barber,
            name='Frizura',
            duration=30,
            description='Brzo šišanje.',
            price=20
        )

       
        self.appointment = Appointment.objects.create(
            user=self.user,
            barber=self.barber,
            time=timezone.now().time(),
            date=(timezone.now() + timedelta(days=1)).date(),
            created_at=timezone.now(),
            is_confirmed=True
        )

        self.review = Reviews.objects.create(
            barber=self.barber,
            user=self.user,
            rating=5,
            comment='Odlična usluga!',
        )

    def test_barber_list_view(self):
        response = self.client.get(reverse('barberwebapp:barber_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.barber.name)

    def test_barber_detail_view(self):
        response = self.client.get(reverse('barberwebapp:barber_detail', args=[self.barber.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.barber.bio)

    def test_service_list_view(self):
        response = self.client.get(reverse('barberwebapp:service_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.service.name)

    def test_service_detail_view(self):
        response = self.client.get(reverse('barberwebapp:service_detail', args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.service.description)

    def test_appointment_list_view(self):
        response = self.client.get(reverse('barberwebapp:appointment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.appointment.barber.name)

    def test_appointment_detail_view(self):
        response = self.client.get(reverse('barberwebapp:appointment_detail', args=[self.appointment.id]))
        self.assertEqual(response.status_code, 200)
        formatted_time = time_filter(self.appointment.time, 'g:i a').lower()
        self.assertContains(response, formatted_time)

    def test_reviews_list_view(self):
        response = self.client.get(reverse('barberwebapp:reviews_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.review.comment)

    def test_reviews_detail_view(self):
        response = self.client.get(reverse('barberwebapp:reviews_detail', args=[self.review.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.review.rating)
