from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    USER_ROLES = (
        ("admin", "admin"),
        ("receptionist", "receptionist"),
        ("doctor", "doctor"),
        ("pharmacist", "pharmacist"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES, default="receptionist")

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Dr. {self.profile.user.last_name} ({self.specialization})"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    symptoms = models.TextField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default="pending")

    def __str__(self) -> str:
        return f"Appointment with Dr. {self.doctor.profile.user.last_name} for {self.patient.first_name} on {self.date}"


class Billing(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    ammount = models.IntegerField()
    mpesa_number = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20, default="unpaid")
    transaction_id = models.CharField(max_length=100, null=True)
    date = models.CharField(default=timezone.now, max_length=100)

    def __str__(self) -> str:
        return f"Billing for {self.appointment.patient.first_name} (Status: {self.payment_status})"


class Receptionist(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Receptionist: {self.profile.user.username}"


class Pharmacist(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Pharmacist: {self.profile.user.username}"
