from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    UserProfile,
    Patient,
    Doctor,
    Appointment,
    Billing,
    Receptionist,
    Pharmacist,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ["id", "user", "role"]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "contact_number",
            "email",
        ]


class DoctorSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = Doctor
        fields = ["id", "profile", "specialization"]


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Appointment
        fields = [
            "id",
            "patient",
            "doctor",
            "date",
            "symptoms",
            "time",
            "status",
        ]


class BillingSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()

    class Meta:
        model = Billing
        fields = [
            "id",
            "appointment",
            "amount",
            "payment_status",
            "transaction_id",
            "date",
        ]


class ReceptionistSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = Receptionist
        fields = ["id", "profile"]


class PharmacistSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = Pharmacist
        fields = ["id", "profile"]
