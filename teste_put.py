import requests

headers = {'Authorization': 'Token 6936346177e3531812b9aca8d895d57ee3178fa3'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "testa put",
    "url": "asdasdas.sadasd.com"
}

result = requests.put(url=f'{url_cursos}6/', headers=headers, data=curso_atualizado)

assert result.status_code == 200
assert result.json()['titulo'] == curso_atualizado['titulo']
