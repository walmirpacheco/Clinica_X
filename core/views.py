from django.shortcuts import render
from .forms import ClienteModelForm, FuncionarioModelForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def Cad_Funcionario(request):
    if str(request.method) == 'POST':
        form = FuncionarioModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            
            messages.success(request, 'Funcionario salvo com sucesso!')
            form = FuncionarioModelForm()
        else:
            messages.error(request, 'Erro ao salvar cliente!')
    else:
            form = FuncionarioModelForm()
    context = {
            'form': form
        }
    return render(request, 'funcionario.html', context)    

def Cad_Cliente(request):
    if str(request.method) == 'POST':
        form = ClienteModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            messages.success(request, 'Cliente salvo com sucesso!')
            form = ClienteModelForm()
        else:
            messages.error(request, 'Erro ao salvar cliente!')
    else:
            form = ClienteModelForm()
    context = {
            'form': form
        }
    return render(request, 'cliente.html', context)    
