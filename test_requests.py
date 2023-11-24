import requests

'''# GET para avaliações
# Fará a requisição do tipo get no end-point/URL
#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/6/')

# Acessa os códigos de status HTTP
#print(avaliacoes)

# Acessa os dados da resposta HTTP
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

# Acessando dados individuais
#print(avaliacoes.json()['results'][2]['nome'])

'''

headers = {'Authorization': 'Token 59b1de81b5aff89b1cb7110806f8fd4597c43a67'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)

print(cursos.json())

