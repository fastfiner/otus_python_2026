import requests

url1 = "https://api.openbrewerydb.org/"
url2 = url1 + "v1/breweries"

my_params = {
    "by_city": "Los+Angeles",
    "by_type": "micro",
}

response = requests.get(url2, params=my_params)
data = response.json()
names = [(brewery["name"], brewery["address_1"]) for brewery in data[:5]]

print("Статус:", response.status_code)
print("Пять мини пивоварнь в Лос-анджелес:")
for name, address in names:
    print(f"   {name}: {address}")
    

# # REST DELETE###########################################################################################################
import requests

response = requests.delete("https://jsonplaceholder.typicode.com/users/1")

if response.status_code == 200:
    print("✅ Пользователь удалён")


# # REST PUT###########################################################################################################

import requests

updated_user = {
    "id": 1,
    "name": "Alice Updated",
    "email": "alice_new@example.com"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
    json=updated_user
)

if response.status_code == 200:
    print("✅ Пользователь обновлён")

# # REST POST###########################################################################################################
import requests

new_user = {
    "name": "Alice",
    "email": "alice@example.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)

if response.status_code == 201:
    created = response.json()
    print(f"Создан пользователь с ID: {created['id']}")


# # REST GET###########################################################################################################
# import requests

# # Получить список всех пользователей
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# users = response.json()
# print(users[0]["name"])  # "Leanne Graham"

# # Получить одного пользователя
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# user = response.json()
# print(user["name"])  # "Leanne Graham"




# # POST ############################################################################################################
# import requests

# url = "https://httpbin.org/post"  # Тестовое API, которое возвращает всё, что вы ему отправили

# # Данные, которые мы отправляем
# my_data = {
#     "name": "Анна",
#     "age": 30,
#     "city": "Москва"
# }

# # Отправляем POST-запрос
# response = requests.post(url, json=my_data)

# # Получаем ответ (сервер вернёт наши данные обратно)
# result = response.json()

# print("Статус:", response.status_code)
# print("Отправленные данные:", result["json"])


# #Параметры запроса GET - запросы ############################################################################################################
# import requests

# # Это наш «адрес» для запроса
# url = "https://api.thecatapi.com/v1/images/search"

# # Это наши «уточнения» для сервера
# my_params = {"limit": 5} # параметры указаны в доке АПИ 

# # Отправляем запрос вместе с уточнениями
# response = requests.get(url, params=my_params)

# # Смотрим, что нам пришло
# data = response.json()
# print(f"Количество картинок: {len(data)}")
# print(data)


# Простой пример ############################################################################################################
# import requests

# # Делаем запрос к API, который всегда работает
# url = "https://api.github.com/zen"
# response = requests.get(url)

# print("Статус:", response.status_code)
# print("Ответ:", response.text)