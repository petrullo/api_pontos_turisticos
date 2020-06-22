from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecosSerializer
from atracoes.models import Atracao

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True, read_only=True)
    endereco = EnderecosSerializer(read_only=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico

        fields = ['id', 'nome', 'descricao', 'foto', 'atracoes', 'comentario',
                  'avaliacao', 'endereco', 'descricao_completa', 'descricao_completa2']
        read_only_fields = ('comentario', 'avaliacao')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objetcs.create(**validated_data)

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)




