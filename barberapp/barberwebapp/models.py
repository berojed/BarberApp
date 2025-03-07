from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number=models.IntegerField(null=True)

class Barber(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    rating = models.IntegerField()

    class Meta: ordering = ['name']

    def __str__(self):
        return self.name

class Service(models.Model):
    barber=models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='services', null=True, blank=True)
    name=models.CharField(max_length=50)
    duration=models.IntegerField()
    description=models.CharField(max_length=50)
    price=models.IntegerField()

    class Meta: ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.price} EUR"
    
class Appointment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    barber=models.ForeignKey(Barber,on_delete=models.CASCADE,related_name="appointments", null=True, blank=True)
    time=models.TimeField()
    date=models.DateField()
    created_at=models.DateTimeField()
    is_confirmed=models.BooleanField(default=False)

    class Meta: ordering = ['date']

    def __str__(self):
        return f"Appointment on {self.date} at {self.time} with {self.barber}"
    
class WorkingHours(models.Model):
    barber = models.OneToOneField(Barber, on_delete=models.CASCADE, related_name="working_hours",null=True, blank=True)
    monday = models.CharField(max_length=50, blank=True, null=True) 
    tuesday = models.CharField(max_length=50, blank=True, null=True)
    wednesday = models.CharField(max_length=50, blank=True, null=True)
    thursday = models.CharField(max_length=50, blank=True, null=True)
    friday = models.CharField(max_length=50, blank=True, null=True)
    saturday = models.CharField(max_length=50, blank=True, null=True)
    sunday = models.CharField(max_length=50, blank=True, null=True)

class Reviews(models.Model):
    barber=models.ForeignKey(Barber,on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews")
    rating=models.PositiveBigIntegerField()
    comment=models.CharField(max_length=100)
    posted_at=models.DateField(auto_now_add=True)

    class Meta: ordering = ['-rating']

    def __str__(self):
        return f"Rating for {self.barber} by {self.user}"
    