import json
from pathlib import Path

path = Path("favorite_number.json")

number = path.read_text()
number = json.loads(number)
print(f"I know your favorite number! It’s {number}.")
