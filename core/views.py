from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Cad_Funcionario(request):
    return render(request, 'funcionario.html')    

def Cad_Cliente(request):
    return render(request, 'cliente.html')    
