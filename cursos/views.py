from django.core.exceptions import BadRequest
from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

"""
    V1 da API
"""


class CursosAPIView(generics.ListCreateAPIView):  # o ListCreate serve para listar uma sequência de itens do db
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):  # Já este argumento permite a modificação de um UNICO objeto
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(),
                                 pk=self.kwargs.get('avaliacao_pk'))


"""
    V2 da API
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])  # Apesar de configurado, a set de paginção não afeta as actions das ViewSets
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2                      # define o número de itens paginados
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(queryset=avaliacoes)       # Define o queryset para ser paginado

        if page is not None:                                     # Se o queryset paginado não for vazio,
            serializer = AvaliacaoSerializer(page, many=True)    # serialize o queryset, com vários elementos
            return self.get_paginated_response(serializer.data)  # E retorne a Response padrão do módulo da paginação

        curso = self.get_object()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

"""
Modo mais rápido para a criação, com todos os métodos disponíveis:
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""


# Neste modo, adicionam-se todas as propriedades do ModelViewSet, mas agora é possível manipular fácilmente quais verbos
# podem ser usados na View;
# Por exemplo, se remover a classe ListModelMixin, não será mais possível listar todas as avaliações na URI
# api/V2/avaliacoes, se remover o DestroyModelMixin, ninguém teria a permissão de deletar a Avaliação
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
