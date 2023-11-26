import requests

# Criar classe para agrupar todos os teste do ambiente/API
class TestCursos:
    
    headers = {'Authorization': 'Token 59b1de81b5aff89b1cb7110806f8fd4597c43a67'}
    url_cursos = 'http://localhost:8000/api/v2/cursos/'
    
    #get_curso_id = 3
    #put_curso_id = 5
    #del_curso_id = 2

    def test_get_all(self):
        resposta = requests.get(url=self.url_cursos, headers=self.headers)
        
        assert resposta.status_code == 200
        #print(resposta.json()['results'])
               
    def test_get_individual(self):
        resposta = requests.get(url=f'{self.url_cursos}5/', headers=self.headers)
        
        assert resposta.status_code == 200
        
    def test_post(self):
        novo = {
            "titulo": "Curso Programação em Assembly",
            "url": "http://www.meuscursos.com.br/prograssembly",
            "ativo": True
        }
        
        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=novo)
        
        assert resposta.status_code == 201
        #assert resposta.json()['titulo'] == novo['titulo']
        #print(resposta.json())
    
    def test_put_curso(self):
        atualizar = {
            "titulo": "Curso HTML + CSS para Profissonais",
            "url": "http://www.meuscursos.com.br/htmlcsspro"
        }
        
        resposta = requests.put(url=f'{self.url_cursos}3/', headers=self.headers, data=atualizar)
        
        assert resposta.status_code == 200
        #assert resposta.json()['titulo'] == atualizar['titulo']
    
    def test_delete(self):
        resposta = requests.delete(url=f'{self.url_cursos}1/', headers=self.headers)
        
        #print(resposta.text)
        assert resposta.status_code == 204 and len(resposta.text) == 0

