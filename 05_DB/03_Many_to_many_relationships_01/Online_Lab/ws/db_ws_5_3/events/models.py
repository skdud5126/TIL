from django.db import models

# Create your models here.


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    participants = models.ManyToManyField(Participant)
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.TextField()