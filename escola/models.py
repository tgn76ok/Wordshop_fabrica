from django.db import models
from django.utils import timezone


class Endereco(models.Model):
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100,blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    num_casa = models.IntegerField()
    def __str__(self):
        return self.cep

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    Cordenador = models.CharField(max_length=255, blank=True)
    data_incricao = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        return self.nome_curso
    
class Aluno(models.Model):
    rgm = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    endereco = models.ForeignKey(Endereco,on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso,on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
    

    

