from rest_framework import serializers
from django.db.models import Avg

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
    
    # Valida a avaliação entre 1 e 5
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avalição deve estar entre 1 e 5')
        
        
class CursoSerializer(serializers.ModelSerializer):
    # Nestede relationship - Efeta desempenho da API
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True) # Importa as avaliaçães para a view
    
    # HyperLinked Related Field - Aconselhável
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    
    # Primary Key Related Field - 
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # O valor desse atributo será gerado por uma função, que será noneada com (get_"nome_do_atributo")
    media_avaliacoes = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes', # Permite que as avaliações do curso sejam exibidas
            'media_avaliacoes'
        )
    
    # Função do atributo (media_avaliacoes), aconselhável implementar em Models.py
    def get_media_avaliacoes(self, obj):
        # obj é o curso
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        
        if media is None:
            return 0
        
        return round(media * 2) / 2