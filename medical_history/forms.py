from django import forms
from .models import MedicalHistory

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['date_of_treatment', 'age', 'condition', 'symptoms', 'diagnosis', 'treatment', 'medications', 'notes']