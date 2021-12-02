import requests

headers = {'Authorization': 'Token 6936346177e3531812b9aca8d895d57ee3178fa3'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Teste Post com Requests",
    "url": "test.post.resquests.com"
}

result = requests.post(url=url_cursos, headers=headers, data=novo_curso)

assert result.status_code == 201

assert result.json()['titulo'] == novo_curso['titulo']