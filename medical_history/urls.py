from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"diagnoses", views.DiagnosisViewSet)
router.register(r"patients", views.PatientViewSet)
router.register(r"patient-diagnoses", views.PatientDiagnosisViewSet)
router.register(r"medications", views.MedicationViewSet)
router.register(r"patient-medications", views.PatientMedicationViewSet)

api_urls = router.urls

urlpatterns = [
    path("dashboard/", views.index, name="index"),
    path("patients/", views.index, name="patients_page"),
    path("medications/", views.index, name="medication_page"),
    path("diagnoses/", views.index, name="diagnosis_page"),
]

urlpatterns += api_urls
