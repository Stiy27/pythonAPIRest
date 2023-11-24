import requests

headers = {'Authorization': 'Token 59b1de81b5aff89b1cb7110806f8fd4597c43a67'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

# Cria o novo curso
novo_curso = {
    "titulo": "Curso Fast React JS",
    "url": "http://www.meuscursos.com.br/freactjs"
}

# Envia/Efetua o cadastro do novo curso
resultado = requests.post(url=url_cursos, headers=headers, data=novo_curso)

#print(resultado.json())

# Testa o status code HTTP 201
assert resultado.status_code == 201

# Testa o titulo do curso criado e o retornado
assert resultado.json()['titulo'] == novo_curso['titulo']