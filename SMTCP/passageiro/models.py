from django.db import models
from django.db.models.constraints import CheckConstraint
from django.core.validators import EmailValidator,MaxLengthValidator,MinLengthValidator
from django.db.models import Q,F
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError





class Passageiro(models.Model):
    Tipo_gene=(
        ('M', 'Masculino'),
        ('F', 'Feminino'),
         
    )
    nome=models.CharField(max_length=50)
    email=models.CharField(max_length=30,validators=[EmailValidator(message="email  invalido")])
    endereco=models.CharField(max_length=60,verbose_name="Endereço")
    celular1=models.CharField(max_length=12)
    celular2=models.CharField(max_length=12, blank=True)
    genero=models.CharField(max_length=1,choices=Tipo_gene,verbose_name="Gênero")
    numeroEmer=models.CharField(max_length=12,verbose_name="Numero de Emergência")
    
    def __str__(self):
        return self.nome
    class Meta:
       
        ordering = ['nome']
    


