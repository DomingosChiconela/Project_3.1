from django.shortcuts import render,get_object_or_404, redirect

from.forms import PassagueiroForm
from.models import Passageiro
from django.contrib import messages
from django.core.paginator import Paginator




def listPassa(request): 
    search = request.GET.get('search')

    if search:
        lista =Passageiro.objects.filter(nome__icontains=search)
        context={
        'lista': lista
            }
    else:
        lista = Passageiro.objects.all()

    context={
        'lista': lista
            }
    return render(request, 'passageiro/list_passa.html', context=context)

def ViewPassa(request,id): 
    li=get_object_or_404(Passageiro, pk=id ) 
    return render(request,'passageiro/passa.html',{'li':li})

def addPassageiro(request):
    if  request.method =="GET":

        form=PassagueiroForm()
        context={
        'form':form
    }
        return render(request,'passageiro/add_passa.html', context=context)  
 
    else:
        form=PassagueiroForm(request.POST)
        if form.is_valid():
            Passageiro=form.save()
            form=PassagueiroForm()
            context={
        'form':form
            }
            return redirect('/passageiro/')
        else:
             context={
        'form':form
    }
    return render(request,'passageiro/add_passa.html', context=context)


def editPassa(request, id):
    passa= get_object_or_404(Passageiro, pk=id)
    form = PassagueiroForm(instance=passa)

    if(request.method == 'POST'):
        form = PassagueiroForm(request.POST, instance=passa)

        if(form.is_valid()):
            passa.save()
            return redirect('/passageiro/')
        else:
            return render(request, 'passageiro/edit_passa.html', {'form': form, 'passa': passa})
    else:
        return render(request, 'passageiro/edit_passa.html', {'form': form, 'passa': passa})
    
    

def  delpassa(request, id):
    passa= get_object_or_404(Passageiro, pk=id)
    passa.delete()
    
    messages.info(request, 'deletado com sucesso.')
    return redirect('/passageiro/')
 
 