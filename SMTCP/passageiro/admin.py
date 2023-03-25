from django.contrib import admin
from .models import Passageiro


@admin.register(Passageiro)
class passagueirosAdmin(admin.ModelAdmin):
    search_fields=('nome',)
    
