from django.urls import path
from .views import PatientCreateView, PatientListView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient-list'),
    path('create/', PatientCreateView.as_view(), name='create-patient'),
]