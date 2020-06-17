from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao']




#['id', 'nome', 'descricao', 'aprovado', 'atracoes', 'comentario', 'avaliacao', 'endereco']