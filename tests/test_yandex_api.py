import pytest
import requests

BASE_URL = "https://ya.ru"




def test_some():
    """
    y
    """
    url = f"{BASE_URL}/sfhfh"
    response = requests.get(url)
    assert response.status_code == 404


# Реализуйте в отдельном модуле (файле) тестовую функцию, которая 
# будет принимать 2 параметра:

# url - значение по умолчанию 
# status_code - значение по умолчанию 200

# Параметры должны быть реализованы через pytest.addoption. Можно положить 
# фикcтуру и тестовую функцию в один файл. Основная задача чтобы ваш тест 
# проверял статус ответа по переданному URL. Например, по несуществующему 
# адресу https://ya.ru/sfhfh должен быть валидным ответ 404

# Пример запуска pytest:

# test_module.py --url=https://mail.ru --status_code=200