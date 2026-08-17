import json
from pathlib import Path

path = Path("favorite_number.json")



if path.exists():
    number = path.read_text()
    number = json.loads(number)
    print(f"I know your favorite number! It’s {number}.")
else:
    favorite_number = int(input("What is your favorite number? "))
    content = json.dumps(favorite_number)
    path.write_text(content)
    print(f"I stored {favorite_number} as your favorite number.")