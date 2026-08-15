import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"


@pytest.mark.parametrize("city", ["Los+Angeles", "New+York", "Chicago"])
def test_breweries_exist_in_city(city):
    """
    Тест 1: Проверяет, что в указанных городах есть хотя бы одна пивоварня.
    Использует параметризацию для трёх городов.
    """
    params = {"by_city": city}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_brewerie_id():
    """
    Тест 2: Проверяет получение пивоварни по конкретному ID.
    Сравнивает ID в ответе с запрошенным, проверяет наличие поля "name".
    """
    brewery_id = "ae7b3174-8be8-4d53-a3a5-9b8240970eea"
    url = f"{BASE_URL}/{brewery_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == brewery_id
    assert "name" in data


def test_brewerie_random():
    """
    Тест 3: Проверяет эндпоинт случайной пивоварни.
    Убеждается, что ответ содержит все основные поля.
    """
    url = f"{BASE_URL}/random"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    # API возвращает список с одним объектом
    brewery = data[0]
    required_fields = ["name", "id", "state_province",
                       "brewery_type", "country", "city"]
    for field in required_fields:
        assert field in brewery


def test_all_breweries_list():
    """
    Тест 4: Проверяет, что список всех пивоварен не пуст.
    """
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.parametrize("brewery_type", ["micro", "nano", "brewpub"])
def test_breweries_by_type(brewery_type):
    """
    Тест 5: Проверяет фильтрацию по типу пивоварни.
    Параметризован тремя типами. Убеждается, что все полученные объекты
    имеют правильный тип.
    """
    params = {"by_type": brewery_type}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for brewery in data:
        assert brewery["brewery_type"] == brewery_type
