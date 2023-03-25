from django import forms 
from .models import Passageiro




class PassagueiroForm(forms.ModelForm):
    
    class Meta:
        model=Passageiro
        fields=('__all__')