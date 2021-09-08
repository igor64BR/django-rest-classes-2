from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    # A string abaixo serve de título para a página
    """
    API dos Cursos
    """
    def get(self, request):  # Função do verbo GET
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data, template_name='cursos')


class AvaliacaoAPIView(APIView):
    """
    API das Avaliações
    """
    def get(self):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True).data
        return Response(serializer, template_name='avaliacoes')
