from django.db import models
from accounts.models import Profile

class Doctor(models.Model):
    profile=models.OneToOneField(Profile, on_delete=models.CASCADE)
    specification=models.CharField(max_length=100)
    experiene=models.IntegerField()
    available_days= models.CharField(max_length=100, blank=True)
    contact_number= models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.profile.user.username} ({self.specification})"