import requests

headers = {'Authorization': 'Token 6936346177e3531812b9aca8d895d57ee3178fa3'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

result = requests.get(url=url_cursos, headers=headers)

print(result.json())

# Testa endpoints

assert result.status_code == 200

assert result.json()['count'] == 6

assert result.json()['results'][0]['titulo'] == 'Curso de teste 12'
