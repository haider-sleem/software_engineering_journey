import json
from pathlib import Path

path = Path("favorite_number.json")

favorite_number = int(input("What is your favorite number? "))
content = json.dumps(favorite_number)
path.write_text(content)

