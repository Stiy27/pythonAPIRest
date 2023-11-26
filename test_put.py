import requests

headers = {'Authorization': 'Token 59b1de81b5aff89b1cb7110806f8fd4597c43a67'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_update = {
    "titulo": "Curso Agile com Scrum",
    "url": "http://www.meuscursos.com.br/agscrum",
    "ativo": True
}

# Utiliza template string para inserir a id do curso na url
atualiza_curso = requests.put(url=f'{url_cursos}9/', headers=headers, data=curso_update)

print(atualiza_curso.json())
print(atualiza_curso.status_code)

# Testa o status code HTTP
assert atualiza_curso.status_code == 200

# Testa o título do curso
assert atualiza_curso.json()['titulo'] == curso_update['titulo']