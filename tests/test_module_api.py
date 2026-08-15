import pytest
import requests


def test_api(url, status_code):
    """
    Тест проверяющий статус запроса
    """
    print(f"Ссылка: {url}, Статус: {status_code}")
    response = requests.get(url)
    assert response.status_code == int(status_code)
