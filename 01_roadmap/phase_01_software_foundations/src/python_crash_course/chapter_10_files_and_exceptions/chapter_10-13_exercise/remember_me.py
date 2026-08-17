import json
from pathlib import Path

path = Path("remember_me.json")

person = {"name": "Ali"}

job = input("What is your job? ")

person["job"] = job

age = int(input("What is your age? "))

person["age"] = age


user = json.dumps(person)
path.write_text(user)

contents = path.read_text()
contents = json.loads(contents)

print(
    f"User information:\n\t{'Name':<4}: {contents['name']}\n\t{'Job':<4}: {contents['job']}\n\t{'Age':<4}: {contents['age']}"
)
