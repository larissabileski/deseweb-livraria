from django.contrib import admin

from livraria.models import Autor, Categoria, Compra, Editora, ItensCompra, Livro

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
# admin.site.register(Compra)
# admin.site.register(ItensCompra)


class ItensCompraInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]
