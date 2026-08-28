import json
from pathlib import Path

path = Path("remember_me.json")


def get_stored_user(path):
    """Return the stored user dictionary if it exists."""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None


def get_new_user(path):
    """Prompt the user for new information and store it."""
    person = {}

    person["name"] = input("What is your name? ")
    person["job"] = input("What is your job? ")
    person["age"] = int(input("What is your age? "))

    contents = json.dumps(person)
    path.write_text(contents)

    return person


def greet_user():
    """Verify the user and print a summary."""
    person = get_stored_user(path)

    if person:
        answer = input(f"Are you {person['name']}? (yes/no): ").lower()

        if answer != "yes":
            person = get_new_user(path)
    else:
        person = get_new_user(path)

    print(
        f"\nUser information:"
        f"\n\t{'Name':<4}: {person['name']}"
        f"\n\t{'Job':<4}: {person['job']}"
        f"\n\t{'Age':<4}: {person['age']}"
    )


greet_user()
