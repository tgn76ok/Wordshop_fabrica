from rest_framework import serializers
from .models import Aluno, Endereco,Curso

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome', 'rgm','endereco','curso']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['cep']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'data_incricao']