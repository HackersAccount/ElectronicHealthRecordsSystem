from django.db import models

# Create your models here.
class Patient(models.Model):
    
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField()
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"

    def __str__(self):
        return self.name

