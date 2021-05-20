from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apiInvest.serializers import UserSerializer, GroupSerializer, ContaSerializer, AtivoSerializer
from .models import Ativo, Conta, Transacao, tipo_transacao, taxa_transacao
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SaldoContaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Ativo.objects.all()
    serializer_class = ContaSerializer
    permission_classes = [permissions.IsAuthenticated]


class CadastroAtivoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer
    permission_classes = [permissions.IsAuthenticated]
