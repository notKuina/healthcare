# doctors/views.py
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

# List all doctors 
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# Retrieve, update, or delete a doctor by id
class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer