import requests
import jsonpath

avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")

# JSONPATH retorna uma lista e 'results' é uma lista de dicionários
#resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# Retorna linsta com o elemento, de avaliaçoes, passado pelo [indice].chave
#firsOfResults = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

# Retorna lista com todos os nomes de todas as avaliacoes
#todosAvaliadores = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

# Retorna lista com todas as notas
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')

print(notas)