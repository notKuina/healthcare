from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    role=models.CharField(max_length=50,choices=[('doctor', 'Doctor'),('patient','Patient')])

    def __str__(self):
        return self.user.username