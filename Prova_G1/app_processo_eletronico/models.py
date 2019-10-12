from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome=models.CharField('Nome completo',max_length=150)
    data_nascimento=models.DateField('Data de nascimento',blank=True,null=True)
    cpf=models.CharField('CPF',max_length=11)
    usuario=models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula=models.CharField("Número da mátriula",max_length=15)
    dataContratacao=models.DateField("Data de Inicio de contrato",auto_now_add=True)

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome=models.CharField("Nome do departamento",max_length=50)

    def __str__(self):
        return self.nome





class Processo(models.Model):
    func=models.ForeignKey(Funcionario,related_name="+",null=True, blank=True, on_delete=models.SET_NULL)
    data_criacao= models.DateTimeField(auto_now_add=True)
    interessados=models.ForeignKey(Pessoa,related_name="+",null=True, blank=True, on_delete=models.SET_NULL)
    investigados=models.ForeignKey(Pessoa,null=True, blank=True, on_delete=models.SET_NULL)

class Documento(models.Model):
    processo=models.ForeignKey(Processo,null=True, blank=True, on_delete=models.SET_NULL)
    titulo=models.CharField("Titulo do Documento",max_length=50)
    data=models.DateTimeField("Data de criação do documento",auto_now_add=True)
    texto=models.CharField("Conteudo do Documento",max_length=99999)
    criador=models.ForeignKey(Funcionario,null=True, blank=True, on_delete=models.SET_NULL)


class Portaria_de_instauração(Documento):
    def __str__(self):
        return self.titulo


class Pedido_de_prazo(Documento):
    just=models.CharField("Justiicativa do pedido de Prazo",max_length=999)
    nova_data=models.DateTimeField("Nova data para o documnto",null=True,blank=True)

    def __str__(self):
        return self.just


class Envio_de_processo(Documento):
    departamento=models.ForeignKey(Departamento,null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.titulo


class Tramite(models.Model):
    processo=models.ForeignKey(Processo,null=True, blank=True, on_delete=models.SET_NULL)
    origem=models.ForeignKey(Departamento,related_name="+",null=True, blank=True, on_delete=models.SET_NULL)
    destino=models.ForeignKey(Departamento,null=True, blank=True, on_delete=models.SET_NULL)
    data_envio = models.DateField(null=True, blank=True)
    data_recebido=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


