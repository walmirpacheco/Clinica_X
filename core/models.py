from django.db import models
from stdimage.models import StdImageField


# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)     
    sexo = models.CharField('Sexo', max_length=10)              
    endereco = models.CharField('Endereço', max_length=100)    
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    trabalho = models.CharField('Trabalho', max_length=50)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def cliente_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(cliente_pre_save, sender=Cliente)  

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)     
    sexo = models.CharField('Sexo', max_length=10)            
    endereco = models.CharField('Endereço', max_length=100)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    trabalho = models.CharField('Trabalho', max_length=50)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def funcionario_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(funcionario_pre_save, sender=Funcionario)