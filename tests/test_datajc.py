import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
data_dir = BASE_DIR / "data"
books_path = data_dir / "books.csv"

with open(books_path, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    books = list(reader)