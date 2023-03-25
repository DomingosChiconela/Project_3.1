from django import forms 
from companhia.models import Companhia,Motorista,Viatura,Rota,Viagem
from django.db.models import Q
from django.forms import CheckboxSelectMultiple



class MotoristaForm(forms.ModelForm):
    
    class Meta:
        model=Motorista
        fields=['nome','email','endereco','genero','celular1','celular2','numeroEmer','companhia']
        
        
        
class ViaturaForm(forms.ModelForm):
    
    
    class Meta:
        model=Viatura
        fields=['Matricula','Marca','Modelo','Cor','companhia']
        
        
        
class RotaForm(forms.ModelForm):
    
    
    class Meta:
        model=Rota
        fields=['nome','distancia','loca']
        
        
class ViagemForm(forms.ModelForm):

    class Meta:
        model=Viagem
        fields=['codigo','partida','chegada','passageiro','motorista','viatura','companhia','rota']
       
