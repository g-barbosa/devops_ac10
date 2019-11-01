"""arquivo"""
from com.faculdadeimpacta.calculadora import app_web_start


def test_root_status():
    """funcao 1"""
    instancia_app = app_web_start.APP.test_client()
    response = instancia_app.get('/')
    assert response.status_code == 200, 'Deveria existir esta rota'


def test_root_url():
    """funcao 2"""
    instancia_app = app_web_start.APP.test_client()
    response = instancia_app.get('/')
    assert response.data.decode('utf-8') == 'Index Page', 'Deveria idont know'
