print("*" * 10)
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

print("*" * 10)
##########################################################

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

print("*" * 10)
##########################################################

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])

print("*" * 10)
##########################################################

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[i])

print("*" * 10)
##########################################################

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

print("*" * 10)
##########################################################
# Update: Instead of using two separate lists, use a dictionary to associate each student with a house.

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

print("*" * 10)
##########################################################

# Update: Instead of looking up each student manually, iterate through the dictionary with a for loop.

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student)

print("*" * 10)
##########################################################

# Update: Print both the student's name (key) and house (value) during the loop.

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

print("*" * 10)
##########################################################

# Update: A student has more than one attribute, so use a list of dictionaries instead.

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"])

print("*" * 10)
##########################################################

# Update: Print another field (house) from each student's dictionary.

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], sep=", ")

print("*" * 10)
##########################################################

# Update: Print all available information for each student.

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(
        student["name"],
        student["house"],
        student["patronus"],
        sep=", ",
    )

print("*" * 10)
##########################################################
