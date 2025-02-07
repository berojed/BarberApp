from django.test import TestCase
from django.utils import timezone
from .models import User, Barber, Service, Appointment, WorkingHours
from django.core.exceptions import ValidationError

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            phone_number=1234567890
        )

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.phone_number, 1234567890)
        self.assertEqual(str(self.user.username), 'testuser')

class BarberModelTest(TestCase):
    def setUp(self):
        self.barber = Barber.objects.create(
            name='Ivica Ivic',
            bio='Sef salona',
            rating=5
        )

    def test_barber_creation(self):
        self.assertTrue(isinstance(self.barber, Barber))
        self.assertEqual(self.barber.name, 'Ivica Ivic')
        self.assertEqual(self.barber.rating, 5)

    def test_barber_ordering(self):
        Barber.objects.create(name='Anica Simic', bio='Zenske frizure', rating=4)
        barbers = Barber.objects.all()
        self.assertEqual(barbers[0].name, 'Anica Simic')
        self.assertEqual(barbers[1].name, 'Ivica Ivic')

class ServiceModelTest(TestCase):
    def setUp(self):
        self.barber = Barber.objects.create(
            name='Ivica Ivic',
            bio='Sef salona',
            rating=5
        )
        self.service = Service.objects.create(
            barber=self.barber,
            name='frizure',
            duration=30,
            description='klasicna frizura',
            price=25
        )

    def test_service_creation(self):
        self.assertTrue(isinstance(self.service, Service))
        self.assertEqual(self.service.name, 'frizure')
        self.assertEqual(self.service.duration, 30)
        self.assertEqual(str(self.service), 'frizure - 25 EUR')

    def test_service_barber_relationship(self):
        self.assertEqual(self.service.barber, self.barber)
        self.assertTrue(self.service in self.barber.services.all())

class AppointmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            phone_number=1234567890
        )
        self.barber = Barber.objects.create(
            name='Ivica Ivic',
            bio='Sef salona',
            rating=5
        )
        self.appointment = Appointment.objects.create(
            user=self.user,
            barber=self.barber,
            time=timezone.now().time(),
            date=timezone.now().date(),
            created_at=timezone.now(),
            is_confirmed=False
        )

    def test_appointment_creation(self):
        self.assertTrue(isinstance(self.appointment, Appointment))
        self.assertEqual(self.appointment.user, self.user)
        self.assertEqual(self.appointment.barber, self.barber)
        self.assertFalse(self.appointment.is_confirmed)

