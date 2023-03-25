from django.db import models
from django.core.validators import EmailValidator,MaxLengthValidator,MinLengthValidator
from django.utils import timezone
from companhia.models import Viagem
class Fiscal(models.Model):
    Tipo_gene=( 
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        
    )
    
    nome=models.CharField(max_length=30)
    email=models.CharField(max_length=30,validators=[EmailValidator(message="email  invalido")])
    endereco=models.CharField(max_length=60,verbose_name="Endereço")
    genero=models.CharField(max_length=1,choices=Tipo_gene,verbose_name="Gênero")
    celular=models.CharField(max_length=12)
    
    viagem=models.ForeignKey(
        Viagem,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
   
    
    
    
