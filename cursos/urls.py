from django.urls import path

from .views import AvaliacaoAPIView, CursoAPIView, CursosAPIView, AvaliacoesAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),

    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes_de_um_objeto'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/',
         AvaliacaoAPIView.as_view(),
         name='unica_aval_do_objeto'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao')
]
