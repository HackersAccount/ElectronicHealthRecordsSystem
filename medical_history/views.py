from typing import Any
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, CreateView

from medical_history.forms import MedicalHistoryForm
from patients.models import Patient
from .models import MedicalHistory

class MedicalHistoryDetailView(DetailView):
    model = MedicalHistory
    template_name = 'medical_history.html'  # replace with your actual template path
    context_object_name = 'patient_history'
    
    def get_object(self, queryset=None):
        patient_id = self.kwargs.get('pk')
        patient = get_object_or_404(Patient, pk=patient_id)
        medical_history = MedicalHistory.objects.filter(patient_id=patient).first()
        if medical_history is None:
            medical_history = MedicalHistory(patient_id=patient)
        return medical_history    

class MedicalHistoryUpdateView(UpdateView):
    model = MedicalHistory
    form_class = MedicalHistoryForm
    template_name = 'edit_medical_history.html'

    def get_success_url(self):
        return reverse('medical_history', kwargs={'pk': self.object.pk})
    
    
class MedicalHistoryCreateView(CreateView):
    model = MedicalHistory
    form_class = MedicalHistoryForm
    template_name = 'create_medical_history.html'

    def get_success_url(self):
        return reverse('medical_history', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_id'] = self.kwargs.get('pk')  
        return context
    

    def form_valid(self, form):
        patient_id = self.kwargs.get('pk')
        patient = Patient.objects.get(pk=patient_id)
        form.instance.patient_id = patient
        return super().form_valid(form)