import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results') //dicionario
# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')

print(resultados)
