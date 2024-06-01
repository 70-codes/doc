from django.contrib import admin
from .models import (
    UserProfile,
    Patient,
    Doctor,
    Appointment,
    Billing,
    Receptionist,
    Pharmacist,
)

admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Billing)
admin.site.register(Receptionist)
admin.site.register(Pharmacist)
