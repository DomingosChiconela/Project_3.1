from django.contrib import admin

from companhia.models import Companhia,Motorista,Rota,Viatura,Viagem
@admin.register(Companhia)
class companhiaAdmin(admin.ModelAdmin):
    search_fields=('nome',)

    
@admin.register(Motorista)
class passagueirosAdmin(admin.ModelAdmin):
   list_filter=('nome',)

@admin.register(Viatura)
class ViaturaAdmin(admin.ModelAdmin):
       pass

@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
       pass
   
   
admin.site.register(Viagem)
