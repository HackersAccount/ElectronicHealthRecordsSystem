from django.urls import path
from .views import MedicationDetailView

urlpatterns = [
    path('<int:pk>/medical_history/', MedicationDetailView.as_view(), name='medication-detail'),
]