from django.contrib import admin
from .models import Aluno, Endereco,Curso

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id',  'nome', 'rgm','endereco')

admin.site.register(Aluno, AlunoAdmin)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'bairro')

admin.site.register(Endereco, EnderecoAdmin)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'data_incricao')

admin.site.register(Curso, CursoAdmin)
