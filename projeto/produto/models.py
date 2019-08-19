from django.db import models

# Create your models here.
# Desenvolvendo o modelo dados de produto
class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField('Produto',max_length=100, unique=True)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('Estoque Atual')
    estoque_minimo = models.PositiveIntegerField('Estoque Mínimo', default=0)

    class Meta:
        ordering = ('produto', )

    def __str__(self):
        return self.produto
