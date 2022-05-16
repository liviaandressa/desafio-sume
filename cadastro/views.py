from django.shortcuts import render
from rest_framework import viewsets

from .models import Contas, Ufs, Cidades, Enderecos, Pessoas, Ocorrencias
from .serializers import ContasSerializer, UfsSerializer, CidadesSerializer, EnderecosSerializer, PessoasSerializer, OcorrenciasSerializer


class ContasViewSet(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContasSerializer

class UfsViewSet(viewsets.ModelViewSet):
    queryset = Ufs.objects.all()
    serializer_class = UfsSerializer

class CidadesViewSet(viewsets.ModelViewSet):
    queryset = Cidades.objects.all()
    serializer_class = CidadesSerializer

class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecosSerializer

class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer

class OcorrenciasViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencias.objects.all()
    serializer_class = OcorrenciasSerializer