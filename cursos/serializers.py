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

    def validate_aval(self, valor):
        if 1 <= valor <= 5:
            return valor
        else:
            raise serializers.ValidationError('Avaliação deve ser entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):  # No fim, essa classe irá JSONar os dados requeridos
    """
    # Nested db relation
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)  # Adiciona uma lista nos cursos de todas as avaliações
                                                                 # daquele curso, com todos os detalhes
    """

    """
    # Hiyperlinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(  # Apresenta uma lista com os links para acessar os itens a partir
        many=True,                                     # do ID deles
        read_only=True,
        view_name='avaliacao-detail'  # nome_do_model-detail
    )"""
    """
    # PK related fields
    avaliacoes = serializers.PrimaryKeyRelatedField(  # Apresenta a lista de id dos itens descendentes
        many=True,
        read_only=True,
    )
    """

    avaliacoes = serializers.StringRelatedField(  # Lista a partir da fun. __str__ do model
        many=True,
        read_only=True
    )

    # Obs: Usar este no desafio para listar os organizadores

    class Meta:
        model = Curso
        fields = (
            'id',
            'curso',
            'url',
            'criado',
            'modificado',
            'ativo',
            'avaliacoes'
        )

