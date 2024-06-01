from django.urls import path
from .views import ManageDoctorView, ManageReceptionistView, ManagePharmacistView

urlpatterns = [
    path("doctor/", ManageDoctorView.as_view(), name="add-doctor"),
    # path("add-doctor/<int:pk>/", ManageDoctorView.as_view(), name="doctor-detail"),
    path("receptionist/", ManageReceptionistView.as_view(), name="add-receptionist"),
    # path(
    #     "add-receptionist/<int:pk>/",
    #     ManageReceptionistView.as_view(),
    #     name="receptionist-detail",
    # ),
    path("pharmacist/", ManagePharmacistView.as_view(), name="add-pharmacist"),
    # path(
    #     "add-pharmacist/<int:pk>/",
    #     ManagePharmacistView.as_view(),
    #     name="pharmacist-detail",
    # ),
]
