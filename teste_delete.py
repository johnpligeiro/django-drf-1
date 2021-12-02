import requests

headers = {'Authorization': 'Token 6936346177e3531812b9aca8d895d57ee3178fa3'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

result = requests.delete(url=f'{url_cursos}6/', headers=headers)

assert result.status_code == 204
assert len(result.text) == 0
