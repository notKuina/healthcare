from django.db import models
from accounts.models import Profile
from doctors.models import Doctor

class Patient(models.Model):
    STATUS_CHOICES = [
        ('checked_in', 'Checked In'),
        ('admitted','Admitted'),
        ('discharged', 'Discharged'),
        ('observation', 'Under Observation'),
    ]

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    age = models.IntegerField()
    medical_history = models.TextField(blank=True)
    disease = models.CharField(max_length=255, blank=True)
    symptoms = models.TextField(blank=True)
    blood_type = models.CharField(max_length=3, blank=True)
    guardian_name = models.CharField(max_length=100, blank=True)
    medical_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='checked_in')

    def __str__(self):
        return f"{self.profile.user.username} ({self.get_medical_status_display()})"

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('patient', 'doctor')