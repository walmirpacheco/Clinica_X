from django.urls import path

from .views import index, Cad_Cliente, Cad_Funcionario

urlpatterns = [
    path('', index, name='index'),
    path('cliente/', Cad_Cliente, name='cliente'),
    path('funcionario/', Cad_Funcionario, name='funcionario'),
]