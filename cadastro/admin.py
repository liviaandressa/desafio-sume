from django.contrib import admin
from .models import Contas, Ufs, Cidades, Enderecos, Pessoas, Ocorrencias


class ContasForm(admin.ModelAdmin):
    list_display = ['conta', 'agencia', 'banco', 'tp_conta']
    search_fields = ['agencia', 'banco', 'tp_conta']

class UfsForm(admin.ModelAdmin):
    list_display = ['nome_uf', 'sigla_uf']
    search_fields = ['nome_uf', 'sigla_uf']


class CidadesForm(admin.ModelAdmin):
    list_display = ['nome_cidade', 'id_uf']
    search_fields = ['nome_cidade']

class EnderecosForm(admin.ModelAdmin):
    list_display = ['logradouro', 'numero', 'bairro', 'id_cidade']
    search_fields = ['logradouro', 'numero', 'bairro', 'id_cidade']

class PessoasForm(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'vinculo']
    search_fields = ['nome', 'cpf', 'vinculo']

class OcorrenciasForm(admin.ModelAdmin):
    list_display = ['data', 'id_pessoa']
    search_fields = ['data', 'id_pessoa']

admin.site.register(Contas, ContasForm)
admin.site.register(Ufs, UfsForm)
admin.site.register(Cidades, CidadesForm)
admin.site.register(Enderecos, EnderecosForm)
admin.site.register(Pessoas, PessoasForm)
admin.site.register(Ocorrencias, OcorrenciasForm)


