import requests

headers = {'Authorization': 'Token 59b1de81b5aff89b1cb7110806f8fd4597c43a67'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

# Apaga o curso passado pela id na template string
delete_curso = requests.delete(url=f'{url_cursos}6/', headers=headers)

#print(delete_curso.status_code)

# Testa status code HTTP para DELETE
assert delete_curso.status_code == 204

# Testa se o retorno está vazio
assert len(delete_curso.text) == 0