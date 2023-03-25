from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path('',views.inicio,name='inicio'),
    path('motorista/',views.listMotorista,name='lista_motorrista'),
    path('addmoto/',views.addMotorista,name='adicionar_motorrista'),
    path('edit_moto/<int:id>', views.editMotorista, name="editando_motorista"),
    path('delete_moto/<int:id>', views.delMotorista, name="elimindo_motorista"),
    
    path('viatura/',views.listViatura,name='lista_viatura'),
    path('addviatu/',views.addViatura,name='adicionar_viatura'),
    path('edit_viatu/<int:id>', views.editViatura, name="editando_viatura"),
    path('delete_viatu/<int:id>', views.delViatura, name="elimindo_passagueiro"),
    
    
    path('rota/',views.listRota,name='lista_viatura'),
    path('addrota/',views.addRota,name='adicionar_rota'),
    path('edit_rota/<int:id>', views.editRota, name="editando_rota"),
    path('delete_rota/<int:id>', views.delrota, name="elimindo_rota"),
    
    path('viagem/',views.listViagem,name='lista_viagem'),
    path('addviagem/',views.addViagem,name='adicionar_viagem'),
    path('edit_viagem/<int:id>', views.editViagem, name="editando_viagem"),
    path('delete_viagem/<int:id>', views.delViagem, name="elimindo_viagem"),
   
    
]