from rest_framework import serializers

from cursos.models import *


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = (  # Atributos a serem salvos em JSON e traduzidos pelo serializer
            'id',
            'curso',
            'nome',
            'email',
            'aval',
            'comentario',
            'criado',
        )
        extra_kwargs = {
            'email': {'write_only': True}  # Protec. de Priv.: Não mostrar o email, quando o JSON for solicitado
                                           # Desta forma, evita empresas enviarem spams para o email do usuário
        }


class CursoSerializer(serializers.ModelSerializer):  # No fim, essa classe irá JSONar os dados requeridos

    class Meta:
        model = Curso
        fields = (
            'id',
            'curso',
            'url',
            'criado',
            'modificado',
            'ativo',
        )
