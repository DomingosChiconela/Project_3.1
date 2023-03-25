from django.db import models
from django.db.models.constraints import CheckConstraint
from django.core.validators import EmailValidator,MaxLengthValidator,MinLengthValidator
from django.db.models import Q,F
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError

from passageiro.models import Passageiro


class Companhia (models.Model):
     nome=models.CharField(max_length=30)
     email=models.CharField(max_length=30,validators=[EmailValidator(message="email  invalido")])
     endereco=models.CharField(max_length=60,verbose_name="Endereço")
     celular=models.CharField(max_length=12)
     create_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now=True)
     
     def __str__(self):
        return self.nome
    
class Motorista(models.Model):
    Tipo_gene=(
        ('F', 'Feminino'),
         ('M', 'Masculino'),
    )
    nome=models.CharField(max_length=30)
    email=models.CharField(max_length=30,validators=[EmailValidator(message="email  invalido")])
    endereco=models.CharField(max_length=60,verbose_name="Endereço")
    genero=models.CharField(max_length=1,choices=Tipo_gene,verbose_name="Gênero")
    celular1=models.CharField(max_length=12)
    celular2=models.CharField(max_length=12, blank=True)
    numeroEmer=models.CharField(max_length=12,verbose_name="Numero de Emergência")
    
    companhia=models.ForeignKey(
        Companhia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    
class Viatura(models.Model):
    Matricula=models.CharField(max_length=15)
    Marca=models.CharField(max_length=30)
    Modelo=models.CharField(max_length=30)
    Cor=models.CharField(max_length=30)
    companhia=models.ForeignKey(
        Companhia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Matricula
    
    
class Rota(models.Model):
   nome=models.CharField(max_length=30)
   distancia=models.CharField(max_length=14,verbose_name="Distância")
   loca=models.CharField(max_length=80,verbose_name="Localização")
   
   create_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)
   def __str__(self):
        return self.nome 
    
    
class Viagem(models.Model):
    codigo=models.CharField(max_length=30)
    partida=models.DateTimeField()
    chegada=models.DateTimeField()
    passageiro=models.ManyToManyField("passageiro.Passageiro")
    motorista=models.ManyToManyField("Motorista")
    
    viatura=models.ForeignKey( Viatura,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,)
    
    companhia=models.ForeignKey(
        Companhia,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    rota=models.ForeignKey(
       Rota,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints=[
            CheckConstraint(check=Q(chegada__gt=F('partida')),name="chegada_partida"),
            UniqueConstraint(fields=['codigo'], name='unique_viagem' ),
            
        ]
        ordering = ['partida']
    
    def __str__(self):
        return self.codigo
    
    def clean(self):
        super().clean()
        
        # verifica se a viatura está sendo usada em outra viagem no intervalo de tempo desejado
        if self.pk is None:  # valida apenas durante a criação de uma nova viagem
            outras_viagens = Viagem.objects.filter(viatura=self.viatura).exclude(pk=self.pk)
            for viagens_existente in outras_viagens:
                if self.partida <= viagens_existente.chegada and self.chegada >= viagens_existente.partida:
                    raise ValidationError("Viatura já está sendo usada em outra viagem.")