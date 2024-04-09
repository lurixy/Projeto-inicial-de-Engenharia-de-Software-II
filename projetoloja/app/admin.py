from django.contrib import admin

# importing all models from app/models.py
from .models import *

admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Cargo)
admin.site.register(TipoLogradouro)
admin.site.register(Tipo)
admin.site.register(Bairro)
admin.site.register(Logradouro)
admin.site.register(Imovel)
admin.site.register(Pessoa)
admin.site.register(Categoria)
admin.site.register(Status)