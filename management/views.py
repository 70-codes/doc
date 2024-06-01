from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import (
    UserProfile,
    Doctor,
    Receptionist,
    Pharmacist,
    Patient,
    Billing,
    Appointment,
)
from .serializers import (
    DoctorSerializer,
    ReceptionistSerializer,
    PharmacistSerializer,
    UserSerializer,
    PatientSerializer,
    BillingSerializer,
    AppointmentSerializer,
)
from django.contrib.auth.models import User
from .permissions import IsAdminUser


class ManageDoctorView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        user_data = request.data.get("user")
        profile_data = request.data.get("profile")
        doctor_data = request.data.get("doctor")

        if not user_data or not profile_data or not doctor_data:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create(**user_data)
        profile = UserProfile.objects.create(user=user, **profile_data)
        doctor = Doctor.objects.create(profile=profile, **doctor_data)

        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            doctor = get_object_or_404(Doctor, pk=pk)
            serializer = DoctorSerializer(doctor)
        else:
            doctors = Doctor.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        user = doctor.profile.user

        user_data = request.data.get("user", {})
        profile_data = request.data.get("profile", {})
        doctor_data = request.data.get("doctor", {})

        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in profile_data.items():
            setattr(doctor.profile, attr, value)
        doctor.profile.save()

        for attr, value in doctor_data.items():
            setattr(doctor, attr, value)
        doctor.save()

        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.profile.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManageReceptionistView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        user_data = request.data.get("user")
        profile_data = request.data.get("profile")
        receptionist_data = request.data.get("receptionist")

        if not user_data or not profile_data or not receptionist_data:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create(**user_data)
        profile = UserProfile.objects.create(user=user, **profile_data)
        receptionist = Receptionist.objects.create(profile=profile, **receptionist_data)

        serializer = ReceptionistSerializer(receptionist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            receptionist = get_object_or_404(Receptionist, pk=pk)
            serializer = ReceptionistSerializer(receptionist)
        else:
            receptionists = Receptionist.objects.all()
            serializer = ReceptionistSerializer(receptionists, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        receptionist = get_object_or_404(Receptionist, pk=pk)
        user = receptionist.profile.user

        user_data = request.data.get("user", {})
        profile_data = request.data.get("profile", {})
        receptionist_data = request.data.get("receptionist", {})

        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in profile_data.items():
            setattr(receptionist.profile, attr, value)
        receptionist.profile.save()

        for attr, value in receptionist_data.items():
            setattr(receptionist, attr, value)
        receptionist.save()

        serializer = ReceptionistSerializer(receptionist)
        return Response(serializer.data)

    def delete(self, request, pk):
        receptionist = get_object_or_404(Receptionist, pk=pk)
        receptionist.profile.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagePharmacistView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        user_data = request.data.get("user")
        profile_data = request.data.get("profile")
        pharmacist_data = request.data.get("pharmacist")

        if not user_data or not profile_data or not pharmacist_data:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create(**user_data)
        profile = UserProfile.objects.create(user=user, **profile_data)
        pharmacist = Pharmacist.objects.create(profile=profile, **pharmacist_data)

        serializer = PharmacistSerializer(pharmacist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            pharmacist = get_object_or_404(Pharmacist, pk=pk)
            serializer = PharmacistSerializer(pharmacist)
        else:
            pharmacists = Pharmacist.objects.all()
            serializer = PharmacistSerializer(pharmacists, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        pharmacist = get_object_or_404(Pharmacist, pk=pk)
        user = pharmacist.profile.user

        user_data = request.data.get("user", {})
        profile_data = request.data.get("profile", {})
        pharmacist_data = request.data.get("pharmacist", {})

        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in profile_data.items():
            setattr(pharmacist.profile, attr, value)
        pharmacist.profile.save()

        for attr, value in pharmacist_data.items():
            setattr(pharmacist, attr, value)
        pharmacist.save()

        serializer = PharmacistSerializer(pharmacist)
        return Response(serializer.data)

    def delete(self, request, pk):
        pharmacist = get_object_or_404(Pharmacist, pk=pk)
        pharmacist.profile.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagePatientView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        patient_data = request.data.get("patient")

        if not patient_data:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )

        patient = Patient.objects.create(**patient_data)

        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            patient = get_object_or_404(Patient, pk=pk)
            serializer = PatientSerializer(patient)
        else:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)

        patient_data = request.data.get("patient", {})

        for attr, value in patient_data.items():
            setattr(patient, attr, value)
        patient.save()

        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def delete(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManageAppointmentView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        appointment_data = request.data.get("appointment")

        if not appointment_data:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )

        appointment = Appointment.objects.create(**appointment_data)

        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            appointment = get_object_or_404(Appointment, pk=pk)
            serializer = AppointmentSerializer(appointment)
        else:
            appointments = Appointment.objects.all()
            serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)

        appointment_data = request.data.get("appointment", {})

        for attr, value in appointment_data.items():
            setattr(appointment, attr, value)
        appointment.save()

        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def delete(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManageBillingView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        billing_data = request.data.get("billing")

        if not billing_data:
            return Response(
                {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
            )

        billing = Billing.objects.create(**billing_data)

        serializer = BillingSerializer(billing)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk:
            billing = get_object_or_404(Billing, pk=pk)
            serializer = BillingSerializer(billing)
        else:
            billings = Billing.objects.all()
            serializer = BillingSerializer(billings, many=True)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     billing = get_object_or_404(Billing, pk=pk)

    #     billing_data = request.data.get("billing", {})

    #     for attr, value in billing_data.items():
    #         setattr(billing, attr, value)
    #     billing.save()

    #     serializer = BillingSerializer(billing)
    #     return Response(serializer.data)

    # def delete(self, request, pk):
    #     billing = get_object_or_404(Billing, pk=pk)
    #     billing.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
