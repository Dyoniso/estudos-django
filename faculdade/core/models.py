from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo

class Produto(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=100)
    custo = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Carrinho(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    id_pedido = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


