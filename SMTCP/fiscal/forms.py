from django import forms 
from models import Fiscal

class FiscalForm(forms.ModelForm):
    
    class Meta:
        model=Fiscal
        fields=['nome','email','endereco','genero','celular']