from django.urls import reverse
from django.views.generic import ListView, CreateView

from medical_history.models import MedicalHistory
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'  # replace with your actual template path
    context_object_name = 'patients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medical_histories'] = MedicalHistory.objects.all()
        return context
    
class PatientCreateView(CreateView):
    model = Patient
    template_name = 'create_patient.html'
    fields = ['name', 'date_of_birth', 'email']
    
    def get_success_url(self):
        # go to patient detail view
        return reverse('create_medical_history', kwargs={'pk': self.object.pk})
    