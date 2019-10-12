from django.contrib import admin
from .models import Pessoa,Funcionario,Tramite,Departamento,Documento,Portaria_de_instauração,Pedido_de_prazo,Envio_de_processo,Processo

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Tramite)
admin.site.register(Departamento)
admin.site.register(Documento)
admin.site.register(Portaria_de_instauração)
admin.site.register(Pedido_de_prazo)
admin.site.register(Envio_de_processo)
admin.site.register(Processo)

