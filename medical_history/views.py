from rest_framework import viewsets
from django.shortcuts import render
from .models import Diagnosis, Patient, PatientDiagnosis, Medication, PatientMedication
from .serializers import (
    DiagnosisSerializer,
    PatientSerializer,
    PatientDiagnosisSerializer,
    MedicationSerializer,
    PatientMedicationSerializer,
)


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = PatientDiagnosisSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class PatientMedicationViewSet(viewsets.ModelViewSet):
    queryset = PatientMedication.objects.all()
    serializer_class = PatientMedicationSerializer


def index(request):
    return render(request, "medical_history/index.html")


def patients_page(request):
    return render(request, "medical_history/patients.html")


def medications_page(request):
    return render(request, "medical_history/medications.html")


def diagnoses_page(request):
    return render(request, "medical_history/diagnoses.html")
