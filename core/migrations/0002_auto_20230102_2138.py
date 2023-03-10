# Generated by Django 2.2.4 on 2023-01-03 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sexo', models.CharField(max_length=10, verbose_name='Sexo')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('trabalho', models.CharField(max_length=50, verbose_name='Trabalho')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(max_length=10, verbose_name='Sexo'),
        ),
    ]
