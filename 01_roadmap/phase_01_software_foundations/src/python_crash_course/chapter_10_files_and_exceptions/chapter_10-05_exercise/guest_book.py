from pathlib import Path

contents = ""
while True:
    name = input("What is your name? ")
    if name.lower() == "exit":
        break
    else:
        contents += name + "\n"

path = Path("guest_book.txt")
path.write_text(contents)
