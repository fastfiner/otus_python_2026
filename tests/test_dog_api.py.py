import requests

url1 = "https://dog.ceo/dog-api/"
url = "https://dog.ceo/api/breed/hound/images/random"

# Это наши «уточнения» для сервера
my_params = {"breed": "hound"} 

# Отправляем запрос вместе с уточнениями
response = requests.get(url, params=my_params)

# Смотрим, что нам пришло
data = response.json()
print("Ссылка на фото гончей:", data["message"])
print(data)



