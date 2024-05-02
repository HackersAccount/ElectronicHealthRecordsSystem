from django.db import models

# Create your models here for medical history
class MedicalHistory(models.Model):
    patient_id = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    date_of_treatment = models.DateField()
    age = models.IntegerField()
    condition = models.CharField(max_length=255)  # The medical condition diagnosed
    symptoms = models.TextField()  # Symptoms reported by the patient
    diagnosis = models.TextField()  # Details of the diagnosis
    treatment = models.TextField()  # Treatment prescribed
    medications = models.TextField()  # Medications prescribed
    attending_physician = models.CharField(max_length=255)  # Doctor who attended to the patient
    notes = models.TextField(blank=True, null=True)  # Any additional notes
            

    def __str__(self):
        return self.patient_id.name