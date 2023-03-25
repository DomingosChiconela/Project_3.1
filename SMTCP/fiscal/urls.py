from django.urls import path
from . import views
urlpatterns = [
    path( 'companhia/', views.nome_companhia, name='nome_compamhia'),
    path('via/<int:id>', views.lista_viagens, name='lista_viagens'),
    path('passageiro/<int:id>',views.nomes_passageiros_viagem, name='nomes_passageiros_viagem'),

    
]