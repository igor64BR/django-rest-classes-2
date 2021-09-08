from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():  # Este pode ser o caso de criar JSONs diferentes para sucesso ou falha
            print('É, foi válido mesmo')
            # serializer = error  # Modificar o serializer
            # serializer.save()
            # return Response(ERROS, status=status.HTTP_400_BAD_REQUEST)  # É AQUI Q ENVIA O JSON COM ERROS
        serializer.is_valid(raise_exception=True)  # is_valid retorna Bool; raise_exception cancela a função, caso
        serializer.save()                          # retorne False
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API das Avaliações
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True).data
        return Response(serializer, template_name='avaliacoes')

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
