from django.contrib import admin

from cursos.models import Avaliacao, Curso

admin.site.register(Curso)  # Neste modelo, apenas apresenta-se o tópico Curso de forma simplificada


@admin.register(Avaliacao)  # Neste modelo, apresenta-se uma tabela com os atributos listados em list_display
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'email', 'aval', 'criado', 'modificado')

