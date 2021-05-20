from django.contrib import admin

# Register your models here.
from .models import Ativo, Conta, Transacao, tipo_transacao, taxa_transacao


@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modalidade', 'valor', 'status', 'data_create', 'date_update')


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('status', 'saldo')


@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('fk_conta', 'fk_tipo_transacao')


@admin.register(tipo_transacao)
class tipo_transacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status')

@admin.register(taxa_transacao)
class taxa_transacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status')
