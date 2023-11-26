import requests

headers = {'Authorization': 'Token 59b1de81b5aff89b1cb7110806f8fd4597c43a67'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultados_get = requests.get(url=url_cursos, headers=headers)

print(resultados_get.json()['results'])
print("\n\nCursos Cadastrados:\n", resultados_get.json()['results'])

#print(resultados_get.status_code)

# Testa o end-point
assert resultados_get.status_code == 200

# Testa título de curso
#assert resultados_get.json()['results'][0]['titulo'] == 'Curso DevOps'
