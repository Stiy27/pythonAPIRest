# PASSO 04
from django.shortcuts import get_object_or_404
from rest_framework import generics

# Somente para API V2
from rest_framework import viewsets
from rest_framework.decorators import action # Permite alterar ações dentro do ModelView
from rest_framework.response import Response
from rest_framework import mixins

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

""" # API V1

# PASSO 04

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    ""
    #API de Cursos
    ""
    # Recupera os dados do curso
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    # Cria um novo curso
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # Verifica se os dados sáo válidos
        serializer.save() # Salva os dados no DB
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    ""
    # API de Avaliações
    ""
    # Recupera as avalizções
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    # Cria uma nova avaliacão
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

"""


# API V1.1
# Lista/Cria novo Curso
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    

# Recupera, atualiza ou deleta um curso 
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    
# Lista/Cria nova avaliação
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    # Sobrescre a função de generics do rest_framework
    def get_queryset(self):
        if self.kwargs.get('curso_pk'): # Pega a id/pk do curso na uri
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk')) # filtra o curso pela id/pk da uri
        return self.queryset.all() # Retorna todas as avaliacoes do curso (id/pk) passado na uri
    
    
# Recupera, Atualiza ou deleta uma avaliação    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    # Sobrescre a função do django.shortcuts
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), # Filtra a id/pk do curso
                                     curso_id=self.kwargs.get('curso_pk'), # Pega a id/pk do curso na uri
                                     pk=self.kwargs.get('avaliacao_pk')) # Pega a id/pk da avaliacao na uri
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk')) # Retorna a avaliacao, se náo existir retorna (não encontrado)


""" 
# API V2
"""

# ViewSet gera apeans operações CRUD de um único Model - ou Curso ou Avaliacao, não gera composto: curso/1/avaliacao
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    # Decorator cria uma nova rota curso-avaliacoes para trazer avaliacoes de determinado curso
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object() # Pega o curso que chama a url
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


"""
# Esta classe/método não permite retorno de avaliação individual, única.
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""


# Esta classe/método permite retornar apenas uma única avaliação identificada pelo 'id'
class AvaliacaoViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet ):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer