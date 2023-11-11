# PASSO 3

from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True} # Impede que o email apareça na apresentação
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
        
class CursoSerializer(serializers.ModelSerializer):
    # Nestede relationship - Efeta desempenho da API
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True) # Importa as avaliaçães para a view
    
    # HyperLinked Related Field - Aconselhável
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    
    # Primary Key Related Field - 
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes' # Permite que as avaliações do curso sejam exibidas
        )
        