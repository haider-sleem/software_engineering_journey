# Ask user for their name
name = input("What's your name? ").strip().title()

def hello(name="World"):
    print('Hello,', name)
if name == "":
    hello()
else:
    hello(name)
