from django.db import models
# from uuid import uuid4

# def generateUUID():
#     return str(uuid4())

# Create your models here.

class Vendedores(models.Model):
    # codigo do vendedor
    # cdvend = models.UUIDField(max_length=36,primary_key=True, default=generateUUID, editable=False)
    cdvend = models.IntegerField(default=0)
    # nome do vendedor
    dsnome = models.CharField(max_length=50)
    # codigo da tabela de preços padrao
    cdtab = models.IntegerField(default=0)
    # data de nascimento
    dtnasc = models.CharField(max_length=10, blank=True, null=True)


class Clientes(models.Model):
    # codigo do cliente
    # cdcl = models.UUIDField(max_length=36,primary_key=True, default=generateUUID, editable=False)
    cdcl = models.IntegerField(default=0)
    # nome do cliente
    dsnome = models.CharField(max_length=50)
    # pessoa fisica/juridica
    idtipo = models.TextField(max_length=2)
    # codigo do vendedor
    cdvend = models.ForeignKey('Vendedores',on_delete=models.CASCADE)
    #limite de credito
    dslim = models.DecimalField(max_digits=100,decimal_places=1, default=0)
 