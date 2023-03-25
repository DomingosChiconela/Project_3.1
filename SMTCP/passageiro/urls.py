from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   
    
    path('lista/',views.listPassa,name='lista_passagueiro'),
    path('view/<int:id>',views.ViewPassa,name='view_passagueiro'),
    path('addpassa/',views.addPassageiro,name='adicionando_passagueiro'),
    path('edit_passa/<int:id>', views.editPassa, name="editando_passagueiro"),
    path('delete_passa/<int:id>', views.delpassa, name="elimindo_passagueiro"),
     

  
   
    
]
