print("*" * 10)
print("Meaw")
print("Meaw")
print("Meaw")
print("*" * 10)
##########################################################
i = 3
while i != 0:
    print("Meaw")
    i -= 1
print("*" * 10)
##########################################################
i = 0
while i < 3:
    print("Meaw")
    i += 1
print("*" * 10)
##########################################################
for i in [0, 1, 2]:
    print("Meaw")
print("*" * 10)
##########################################################
for _ in range(3):
    print("Meaw")
print("*" * 10)
##########################################################
print("Meaw\n" * 3)
print("*" * 10)
##########################################################
print("Meaw\n" * 3, end="")
print("*" * 10)
##########################################################
while True:
    n = int(input("what is n? "))
    if n <= 0:
        continue
    else:
        break

for _ in range(n):
    print("Meaw")
print("*" * 10)


##########################################################
def main():
    number = get_number()
    meaw(number)


def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n


def meaw(n):
    for _ in range(n):
        print("Meaw")


main()

print("*" * 10)
##########################################################
