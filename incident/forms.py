from django import forms
from .models import Incident, TypeIncident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'date_incident', 'description', 'location', 'area', 'incident_type', 'image']

class TypeIncidentForm(forms.ModelForm):
    class Meta:
        model = TypeIncident
        fields = ['type_name']