from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Ativo, Conta, Transacao, tipo_transacao, taxa_transacao


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conta
        fields = ['saldo', 'status']


class AtivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ativo
        fields = ['nome', 'modalidade', 'status', 'valor']
