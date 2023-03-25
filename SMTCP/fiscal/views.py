from django.shortcuts import render,get_object_or_404
from companhia.models import Viagem,Companhia,Motorista,Viatura
from django.core.paginator import Paginator



def nome_companhia(request):
    search = request.GET.get('search')
    if search:
     compa= Companhia.objects.filter(nome__icontains=search)
        
     context={
        'compa': compa
            }
    else:
       compa=Companhia.objects.all()
       
    context={
        'compa': compa
            }
    return render(request, 'fica/lista_companhia.html', context=context)


def lista_viagens(request,id):
    companhia = Companhia.objects.get(id=id)
    viagens = companhia.viagem_set.all()
    context = {'companhia': companhia, 'viagens': viagens}
    return render(request, 'fica/lista_viagens.html', context=context)

def nomes_passageiros_viagem(request,id):
    viagem = get_object_or_404(Viagem, pk=id)
   
    
    passageiros = viagem.passageiro.all()
    motorrista= viagem.motorista.all()
    
    viatura = viagem.viatura
    
    paginator = Paginator( passageiros,5)
    page = request.GET.get('page')
    passageiros= paginator.get_page(page)
    return render(request, 'fica/lista.html', {'passageiros': passageiros,'motorrista' : motorrista ,'viatura' : viatura ,'viagem': viagem })




