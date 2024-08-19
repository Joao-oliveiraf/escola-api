from django.contrib import admin
from .models import Estudante, Cursos, Matricula

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'cpf']
    list_display_links = ['id', 'nome']
    list_per_page = 10
    search_fields = ['nome',]

class CursoAdmin(admin.ModelAdmin):
    list_display = ['id','codigo', 'descricao', 'nivel_do_curso']
    list_display_links = ['codigo', 'descricao']
    list_per_page = 10
    search_fields = ['codigo']
    
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id','estudante', 'curso', 'periodo']


admin.site.register(Estudante, EstudanteAdmin)
admin.site.register(Cursos, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)