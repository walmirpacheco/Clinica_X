from django import forms
from .models import Cliente, Funcionario

class FuncionarioModelForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        fields = ['nome', 'sexo', 'endereco', 'cidade']

class ClienteModelForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'endereco', 'cidade']