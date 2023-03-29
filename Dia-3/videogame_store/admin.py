from django.contrib import admin

# Register your models here.
from .models import jogo, loja


class jogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


admin.site.register(jogo, jogoAdmin)


class jogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')


admin.site.register(loja)
