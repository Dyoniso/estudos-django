from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    custo = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_nome_completo = models.CharField(max_length=255)
    cliente_telefone = models.CharField(max_length=255)
    cliente_email = models.CharField(max_length=255)
    id_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.id


