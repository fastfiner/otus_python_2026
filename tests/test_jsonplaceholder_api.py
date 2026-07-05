import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_user_has_fields(user_id):
    """
    Тест проверяет, что у пользователя с указанным ID присутствуют
    обязательные поля: name, username, phone.
    """
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()

    for field in ["name", "username", "phone"]:
        assert field in data


def test_post():
    """
    Тест проверяет создание нового поста через POST.
    """
    url = f"{BASE_URL}/posts"
    new_post = {
        "title": "Мой пост",
        "body": "Текст о себе",
        "userId": 1
    }

    response = requests.post(url, json=new_post)

    assert response.status_code == 201
    data = response.json()

    assert "id" in data
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert data["userId"] == new_post["userId"]


def test_put():
    """
    Тест проверяет полное обновление поста через PUT.
    """
    url = f"{BASE_URL}/posts/1"
    updated_post = {
        "id": 1,
        "title": "Обновлённый заголовок",
        "body": "Новый текст",
        "userId": 1
    }

    response = requests.put(url, json=updated_post)

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == updated_post["title"]
    assert data["body"] == updated_post["body"]
    assert data["userId"] == updated_post["userId"]


def test_patch():
    """
    Тест проверяет частичное обновление задачи.
    """
    url = f"{BASE_URL}/todos/1"
    update_data = {"completed": True}

    response = requests.patch(url, json=update_data)

    assert response.status_code == 200
    data = response.json()

    assert data["completed"] == update_data["completed"]


@pytest.mark.parametrize("post_id", [5, 7, 9])
def test_delete_some_post(post_id):
    """
    Тест проверяет удаление поста через DELETE.
    Проверяется статус 200. (Симмуляция удаления)
    """
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.delete(url)

    assert response.status_code == 200
