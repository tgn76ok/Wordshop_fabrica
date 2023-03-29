from django.db import models

# Create your models here.


class jogo(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome, self.preco


class loja(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
