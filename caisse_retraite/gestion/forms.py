from django import forms
from .models import Adherent

class AdherentForm(forms.ModelForm):
    class Meta:
        model = Adherent
        fields = ['nom', 'prenom', 'date_naissance', 'numero_securite_sociale']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }