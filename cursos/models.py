from django.db import models


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)  # Automaticamente salva a data do sistema quando é criado
    modificado = models.DateTimeField(auto_now=True)  # Salva a data e hora no horário da manutenção
    ativo = models.BooleanField(default=True)  # Define se o objeto está atualmente ativo ou não

    class Meta:
        abstract = True
        # A classe é abstrata para que não possa ser considerada como um Model, ou seja, só servirá como base para
        # demais modelos futuros. Dessa forma, não poderá ser criado um Form baseado na class Base
        ordering = ['id']  # Ordena de forma crescente


class Curso(Base):
    curso = models.CharField(max_length=200)
    url = models.URLField(unique=True)  # Define que, para cada objeto Curso, haverá uma URL diferente

    class Meta:                         # Opc.; Adiciona metadados, ou seja, atributos a serem lidos apenas pela
        verbose_name = 'Curso'          # Framework, sem se tornar parte do formulário
        verbose_name_plural = 'Cursos'  # (https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options)
        ordering = ['-id']  # Ordena de forma decrescente

    def __str__(self):
        return self.curso


class Avaliacao(Base):
    curso = models.ForeignKey(to=Curso, on_delete=models.CASCADE, related_name='avaliacoes')
    nome = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    # aval = models.DecimalField(max_digits=2, decimal_places=1)
    aval = models.CharField(max_length=2, blank=True)
    comentario = models.TextField(max_length=500, blank=True, default='')

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']  # Este define que só é permitido 1 comentário pra cada email e curso

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso}: Nota {self.aval}'

