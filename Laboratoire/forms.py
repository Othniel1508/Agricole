from django import forms
from .models import LabResearch


class LabResearchForm(forms.ModelForm):
    class Meta:
        model = LabResearch
        fields = ['id_lab', 'prevision_meteo']
