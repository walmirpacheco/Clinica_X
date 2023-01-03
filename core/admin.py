from django.contrib import admin

from .models import Cliente

from .models import Funcionario


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'sexo', 'endereco', 'cidade', 'modificado', 'ativo')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado', 'sexo', 'endereco', 'cidade', 'modificado', 'ativo')    