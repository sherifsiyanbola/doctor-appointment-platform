from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    patient_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    doctor_feedback = models.TextField(blank=True, null=True)
    doctor_comment = models.TextField(blank=True, null=True)
    doctor = models.CharField(max_length=100, choices=(
        ('sule', 'Dr Mathew Sule - Dentist'),
        ('isa', 'Dr Abubakar Isa - Surgeon'),
        ('zaharadden', 'Dr zaharadden - Opthalmologist'),
        ('kareem', 'Dr Abdulkareem - Cardiologist'),
        ('lawan', 'Dr Abba Lawan - Endocrinologist'),
        ('kano', 'Isa Kano - Gynecologist')
    ))
    date = models.CharField(max_length=100)
    choose_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=(
        ('Appointment under Review', 'Appointment under Review'),
        ('Appointment Accepted', 'Appointment Accepted'),
        ('Appointment Rejected', 'Appointment Rejected')
    ))
    patient_attended_to = models.CharField(max_length=100, blank=True, null=True, choices=(
        ('Yes', 'Yes'),
        ('No', 'No')
    ))
    # image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
    