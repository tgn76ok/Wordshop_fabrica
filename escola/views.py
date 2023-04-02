from django.shortcuts import render

from rest_framework import viewsets
from .serializer import AlunoSerializer,EnderecoSerializer 
from .models import Aluno,Endereco

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    
    serializer_class = EnderecoSerializer


