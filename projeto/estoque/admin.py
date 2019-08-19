from django.contrib import admin
from .models import Estoque, EstoqueItens

# Register your models here.


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline, )
    list_display = (
        '__str__',
        'funcionario',
        'nota_fiscal',
        'movimento',
    )
    search_fields = ('nota_fiscal', )
    list_filter = ('funcionario',)
    date_hierarchy = 'created'



@admin.register(EstoqueItens)
class EstoqueItensAdmin(admin.ModelAdmin):
    list_display = (
    'estoque',
    'produto',
    'quantidade',
    'saldo',
    )
