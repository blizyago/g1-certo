from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome=models.CharField('Nome completo',max_length=150)
    data_nascimento=models.DateField('Data de nascimento',blank=True,null=True)
    cpf=models.CharField('CPF',max_length=11)
    usuario=models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


class Tramite(models.Model):
    data_tramite = models.DateTimeField(auto_now_add=True)
    nome=models.CharField("Nome do Tramite",max_length=50)
    staus=models.BooleanField("Foi recebido ?",default=False)

    def __str__(self):
        return self.nome



class Departamento(models.Model):
    nome_dep=models.CharField("Nome do departamento",max_length=80)
    tramite_enviado=models.ManyToManyField(Tramite)
    tramite_recebido=models.ManyToManyField(Tramite,related_name="+")

    def __str__(self):
        return self.nome_dep


class Documento(models.Model):
    data=models.DateTimeField("Data de criação do documento",auto_now_add=True)


class Portaria_de_instauração(Documento):
    pass


class Pedido_de_prazo(models.Model):

    data = models.DateTimeField("Data de criação do documento", auto_now_add=True)
    just=models.CharField("Justiicativa do pedido de Prazo",max_length=999)
    nova_data=models.DateTimeField("Nova data para o documnto",null=True,blank=True)


class Envio_de_processo(models.Model):
    data = models.DateTimeField("Data de criação do documento", auto_now_add=True)
    departamento=models.ForeignKey(Departamento,null=True, blank=True, on_delete=models.SET_NULL)
    tempo_permanencia=models.CharField("Tempo em 'dais' que o processo passou no departamento",max_length=2)


class Processo(models.Model):
    data_criacao= models.DateTimeField(auto_now_add=True)
    documentos = models.ManyToManyField(Documento, related_name="+")
    interessados=models.ForeignKey(Pessoa,related_name="+",null=True, blank=True, on_delete=models.SET_NULL)
    investigados=models.ForeignKey(Pessoa,null=True, blank=True, on_delete=models.SET_NULL)
    tramites=models.ForeignKey(Tramite,null=True, blank=True, on_delete=models.SET_NULL)
    documentos=models.ManyToManyField(Documento,related_name="+")
    pedido=models.ForeignKey(Pedido_de_prazo,null=True, blank=True, on_delete=models.SET_NULL)
    envios=models.ForeignKey(Envio_de_processo,null=True, blank=True, on_delete=models.SET_NULL)





