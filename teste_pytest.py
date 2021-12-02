import requests


class TestCursos:
    headers = {'Authorization': 'Token 6936346177e3531812b9aca8d895d57ee3178fa3'}
    url_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_cursos}4/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "teste post pytest2",
            "url": "test.post.pytest"
        }
        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "test put cursos pytest",
            "url": "http://www.testputpytest.com"
        }

        resposta = requests.put(url=f'{self.url_cursos}6/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "test put cursos pytest66",
            "url": "http://www.testputpytest.com88"
        }

        resposta = requests.put(url=f'{self.url_cursos}6/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_cursos}5/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
