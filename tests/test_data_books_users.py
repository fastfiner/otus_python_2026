import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
data_dir = BASE_DIR / "data"

books_path = data_dir / "books.csv"
users_path = data_dir / "users.json"

# Чтение csv
# DictReader объект, который умеет читать CSV-файл построчно
with open(books_path, newline='', encoding='utf-8') as f:
    books = list(csv.DictReader(f))
print(f"Книг загружено: {len(books)}")

# Чтение json
with open(users_path, 'r', encoding='utf-8') as f:
    users = json.load(f)
print(f"Пользователей загружено: {len(users)}")

# Распределяем книги между пользователями
total_books = len(books)
total_users = len(users)

books_per_user = total_books // total_users
extra = total_books % total_users

start = 0
for i, user in enumerate(users):
    count = books_per_user + (1 if i < extra else 0)
    user["books"] = books[start:start + count]
    start += count

output_path = BASE_DIR / "result.json"

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(users, f, indent=4, ensure_ascii=False)
