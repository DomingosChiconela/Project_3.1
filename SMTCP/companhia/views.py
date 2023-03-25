from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from.models import Companhia
from.forms import MotoristaForm,ViaturaForm,RotaForm,ViagemForm
from.models import Motorista,Viatura,Rota,Viagem
from django.contrib import messages
from django.core.paginator import Paginator
 
 
 
 
def inicio(request): 
    return render(request, 'base/teste.html')

def listMotorista(request): 
    search = request.GET.get('search')

    if search:
        lista = Motorista.objects.filter(nome__icontains=search)
        context={
        'lista': lista
            }
    else:
        lista = Motorista.objects.all()
    context={
        'lista': lista
            }
    return render(request, 'Motorista/list_moto.html', context=context)



def addMotorista(request):
    if  request.method =="GET":

        form=MotoristaForm()
        context={
        'form':form
    }
        return render(request,'Motorista/add_moto.html', context=context)  
 
    else:
        form=MotoristaForm(request.POST)
        if form.is_valid():
            Motorista=form.save()
            form=MotoristaForm()
            context={
        'form':form
            }
            return redirect('/motorista/')
        else:
             context={
        'form':form
    }
    return render(request,'Motorista/add_moto.html', context=context)



def editMotorista(request, id):
    moto= get_object_or_404(Motorista, pk=id)
    form = MotoristaForm(instance=moto)

    if(request.method == 'POST'):
        form = MotoristaForm(request.POST, instance=moto)

        if(form.is_valid()):
            moto.save()
            return redirect('/motorista/')
        else:
            return render(request, 'Motorista/edit_moto.html', {'form': form, 'moto': moto})
    else:
        return render(request, 'Motorista/edit_moto.html', {'form': form, 'moto': moto})
    
def  delMotorista(request, id):
    moto= get_object_or_404(Motorista, pk=id)
    moto.delete()
    
    messages.info(request, 'deletado com sucesso.')
    return redirect('/motorista/')
 
 
 
def listViatura(request): 
    search = request.GET.get('search')

    if search:
        lista = Viatura.objects.filter(Matricula__icontains=search)
        context={
        'lista': lista
            }
    else:
        lista = Viatura.objects.all()
    context={
        'lista': lista
            }
    return render(request, 'viatura/list_viatura.html', context=context)


def addViatura(request):
    if  request.method =="GET":

        form=ViaturaForm()
        context={
        'form':form
    }
        return render(request,'viatura/add_viatura.html', context=context)  
 
    else:
        form=ViaturaForm(request.POST)
        if form.is_valid():
            Viatura=form.save()
            form=ViaturaForm()
            context={
        'form':form
            }
            return redirect('/viatura/')
        else:
             context={
        'form':form
    }
    return render(request,'viatura/add_viatura.html', context=context)



def editViatura(request, id):
    viatu= get_object_or_404(Viatura, pk=id)
    form = ViaturaForm(instance=viatu)

    if(request.method == 'POST'):
        form = ViaturaForm(request.POST, instance=viatu)

        if(form.is_valid()):
            viatu.save()
            return redirect('/viatura/')
        else:
            return render(request, 'viatura/edit_viatura.html', {'form': form, 'viatu': viatu})
    else:
        return render(request, 'viatura/edit_viatura.html', {'form': form, 'viatu': viatu})
    
    
def  delViatura(request, id):
    viatu= get_object_or_404(Viatura, pk=id)
    viatu.delete()
    
    messages.info(request, 'deletado com sucesso.')
    return redirect('/viatura/')



def listRota(request): 
    search = request.GET.get('search')

    if search:
        lista = Rota.objects.filter(nome__icontains=search)
        context={
        'lista': lista
            }
    else:
        lista = Rota.objects.all()
    context={
        'lista': lista
            }
    return render(request, 'Rota/list_rota.html', context=context)



def addRota(request):
    if  request.method =="GET":

        form=RotaForm()
        context={
        'form':form
    }
        return render(request,'Rota/add_rota.html', context=context)  
 
    else:
        form=RotaForm(request.POST)
        if form.is_valid():
            Rota=form.save()
            form=RotaForm()
            context={
        'form':form
            }
            return redirect('/rota/')
        else:
             context={
        'form':form
    }
    return render(request,'Rota/add_rota.html', context=context)


def editRota(request, id):
    rota= get_object_or_404(Rota, pk=id)
    form = RotaForm(instance=rota)

    if(request.method == 'POST'):
        form = RotaForm(request.POST, instance=rota)

        if(form.is_valid()):
            rota.save()
            return redirect('/rota/')
        else:
            return render(request, 'Rota/edit_rota.html', {'form': form, 'rota': rota})
    else:
        return render(request, 'Rota/edit_rota.html', {'form': form, 'rota': rota})
    
    
def  delrota(request, id):
    rota= get_object_or_404(Rota, pk=id)
    rota.delete()
    
    messages.info(request, 'deletado com sucesso.')
    return redirect('/rota/')



def listViagem(request): 
    search = request.GET.get('search')

    if search:
        lista = Viagem.objects.filter(codigo__icontains=search)
        context={
        'lista': lista
            }
    else:
        lista = Viagem.objects.all()
    context={
        'lista': lista
            }
    return render(request, 'viagem/list_viagem.html', context=context)



def addViagem(request):
    if  request.method =="GET":

        form=ViagemForm()
        context={
        'form':form
    }
        return render(request,'viagem/add_viagem.html', context=context)  
 
    else:
        form=ViagemForm(request.POST)
        if form.is_valid():
            Viagem=form.save()
            form=ViagemForm()
            context={
        'form':form
            }
            return redirect('/viagem/')
        else:
             context={
        'form':form
    }
    return render(request,'viagem/add_viagem.html', context=context)




def editViagem(request, id):
    via = get_object_or_404(Viagem, pk=id)
    form = ViagemForm(instance=via)

    if request.method == 'POST':
        form = ViagemForm(request.POST, instance=via)

        if form.is_valid():
            via = form.save(commit=False)
            via.save()
            form.save_m2m()  # salva as relações muitos-para-muitos
            return redirect('/viagem/')
        else:
            return render(request, 'viagem/edit_viagem.html', {'form': form, 'via': via})
    else:
        return render(request, 'viagem/edit_viagem.html', {'form': form, 'via': via})

    
    
    
def  delViagem(request, id):
    via= get_object_or_404(Viagem, pk=id)
    via.delete()
    
    messages.info(request, 'deletado com sucesso.')
    return redirect('/viagem/')