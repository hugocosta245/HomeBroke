from django.db import models
from django.conf import settings


# Create your models here.
class Base(models.Model):
    data_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Ativo(Base):
    STATUS_ATIVO = (
        ('A', 'Ativo'),
        ('D', 'Deletado'),
    )
    MODALIDADE_ATIVO = (
        ('RF', 'Renda fixa'),
        ('RV', 'Renda variável'),
        ('CP', 'Criptomoeda'),
    )
    nome = models.CharField(max_length=60)
    modalidade = models.CharField(max_length=2, choices=MODALIDADE_ATIVO)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=1, choices=STATUS_ATIVO)

    class Meta:
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'

    def __str__(self):
        return self.nome


class Conta(Base):
    STATUS_CONTA = (
        ('A', 'Ativo'),
        ('D', 'Desativado'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CONTA)
    saldo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        return str(self.fk_user)


class tipo_transacao(Base):
    STATUS_TIPO_TRANSACAO = (
        ('A', 'Ativo'),
        ('D', 'Desativado'),
    )
    nome = models.CharField(max_length=60)
    status = models.CharField(max_length=1, choices=STATUS_TIPO_TRANSACAO)

    class Meta:
        verbose_name = 'Tipo transação'
        verbose_name_plural = 'Tipos de Transações'

    def __str__(self):
        return self.nome

class taxa_transacao(Base):
    STATUS_TIPO_TAXA_TRANSACAO = (
        ('A', 'Ativo'),
        ('D', 'Desativado'),
    )
    fk_tipo_transacao = models.ForeignKey(tipo_transacao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=60)
    status = models.CharField(max_length=1, choices=STATUS_TIPO_TAXA_TRANSACAO)

    class Meta:
        verbose_name = 'Taxa de transação'
        verbose_name_plural = 'Taxas de Transações'

    def __str__(self):
        return self.nome

class Transacao(Base):
    fk_conta = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name='Conta')
    fk_tipo_transacao = models.ForeignKey(tipo_transacao, on_delete=models.CASCADE, verbose_name='Tipo de transação')

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'

    def __str__(self):
        return str(self.fk_conta)
