from django.urls import path
from .views import MedicalHistoryDetailView, MedicalHistoryUpdateView, MedicalHistoryCreateView

urlpatterns = [
    path('<int:pk>/', MedicalHistoryDetailView.as_view(), name='medical_history'),
    path('<int:pk>/edit/', MedicalHistoryUpdateView.as_view(), name='edit_medical_history'),
    path('<int:pk>/create/', MedicalHistoryCreateView.as_view(), name='create_medical_history')
]