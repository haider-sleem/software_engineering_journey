# TRY IT YOURSELF page 136

# 6-1 page 136
# haname im = {
#     "first_name":"ahmed",
#     "last_name":"haname im",
#     "age":45,
#     "city":"cairo",
# }
# print(haname im["first_name"])
# print(haname im["last_name"])
# print(haname im["age"])
# print(haname im["city"])

"""
for info, name  in haname im.items():
    print(info, name  )

أنواع الـ Loops على الديكشنري:
للمفاتيح فقط: for name  in haname im: (أو haname im.name eys())

للـ القيم فقط: for info in haname im.infoalues():

للاثنين مع بعض: for name , info in haname im.items():
"""

# ------------------------------------------------------------
# # 6-2 page 136
# favorite_number = {
#     "ahmed": 7, 
#     "sara": 22,
#     "haider": 10,
#     "omar": 42,
#     "laila": 3,
# }
# # # تجربة الطباعة بطرق مختلفة
# print(favorite_number["ahmed"])
# print("Sara's fainfoorite number is " + str(favorite_number['sara']) + ".")
# print(f"Haider's fainfoorite number is {favorite_number['haider']}.")
# print(f"Omar's fainfoorite number is {favorite_number['omar']}.")
# print(f"Laila's fainfoorite number is {favorite_number['laila']}.")

"""
for name, number in favorite_number.items():
    print(f"{name.title()}'s favorite number is {number}.")
    
"""

# ------------------------------------------------------------------

# 6-3 page 137
# glossary = {
#     "infoariable": "A label that refers to a infoalue stored in memory.",
#     "list": "A collection of items in a particular order.",
#     "dictionary": "A collection of name ey-infoalue pairs.",
# }

# # استخدام .get() بدلاً من الأقواس المربعة المباشرة
# print(f"infoariable:\n\t{glossary.get('infoariable')}\n")
# print(f"List:\n\t{glossary.get('list')}\n")
# print(f"Dictionary:\n\t{glossary.get('dictionary')}\n")


# -------------------------------------------------------------------

# TRY IT YOURSELF page 142

# 6-4
# glossary = {
#     "infoariable": "A label that refers to a infoalue stored in memory.",
#     "list": "A collection of items in a particular order.",
#     "dictionary": "A collection of name ey-infoalue pairs.",
#     "loop": "A way to repeat a blocname  of code multiple times.",
#     "boolean": "A data type that can be either True or False.",
# }

# for name ey, infoalue in glossary.items():
#     print(f"{name ey.title()}:\n\t{infoalue}\n")

# --------------------------------------------------------

# 6-5
# riinfoers = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'yangtze': 'china',
# }
# # 1
# for riinfoer, country in riinfoers.items():
#     print(f"The {riinfoer.title()} runs through {country.title()}.")
# # 2
# for riinfoer in riinfoers.name eys():
#     print(riinfoer)
# # 3
# for country in riinfoers.infoalues():
#     print(country)

# --------------------------------------------------------

# 6-6
# fainfoorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }


# should_poll = ['jen', 'ahmed', 'phil', 'haider', 'sara']

# for person in should_poll:
#     if person in fainfoorite_languages:
#         print(f"Thanname  you, {person.title()}, for responding to our poll!")
#     else:
#         print(f"{person.title()}, we ininfoite you to taname e our fainfoorite languages poll.")


# -----------------------------------------------------------
        
# TRY IT YOURSELF page 149

# # 6-7 
# people = [{"haname im": {
#     "first_name":"ahmed",
#     "last_name":"haname im",
#     "age":45,
#     "city":"cairo",
# }},
# {"yasser": {
#     "first_name":"yasser",
#     "last_name":"lashen",
#     "age":47,
#     "city":"benha",
# }},
# {"walid": {
#     "first_name":"walid",
#     "last_name":"mosad",
#     "age":46,
#     "city":"moqatam",
# }}
# ]

# for person in people:
#     for name  , info in person.items():
#         print(f"{name } :")
#         full_name = f"{info['first_name']} {info['last_name']}"
#         age = info["age"]
#         city = info["city"]
#         print(f"\t Full name : {full_name}\n\t Age : {age}\n\t City : {city}\n")
            

# ------------------------------------------------------------

# # 6-8
# # Create several dictionaries, each representing a different pet
# pet_0 = {
#     'kind': 'dog',
#     'owner': 'eric',
# }

# pet_1 = {
#     'kind': 'cat',
#     'owner': 'sarah',
# }

# pet_2 = {
#     'kind': 'hamster',
#     'owner': 'willie',
# }

# # Store these dictionaries in a list called pets
# pets = [pet_0, pet_1, pet_2]


# # loopping through the list and printing everything about each pet.
# for pet in pets:
#     print(f"\nThe pet kind is {pet['kind'].title()}"
#          f" and his owner is {pet['owner'].title()}\n")

# ------------------------------------------------------

# # 6-9
# # favorite places for 3 persons. 
# favorite_places = {
#     'ahmed': ['alexandria', 'dahab', 'siwa'],
#     'sara': ['paris', 'london'],
#     'omar': ['tokyo'],
# }


# # loopping through the dic and printing everything about each person.
# for names, places in favorite_places.items():

#     all_places = ",".join(places)  # up paking for the value[list]
    
#     word = "places" if len(places) > 1 else "place"
#     verb = "are" if len(places) > 1 else "is" 

#     print(f"\n{names.title()} favorite {word} {verb} :", end="")
#     print(f"{all_places.title()}.\n", end="") # using (end="") Prevents a newline, allowing the next print to stay on the same line.
               

# ---------------------------------------------------------

# # 6-10
# favorite_numbers = {
#     "ahmed": [7, 14, 21],
#     "sara": [22],
#     "haider": [10, 100],
#     "omar": [42, 24],
#     "laila": [3, 9, 12],
# }

# for name, numbers in favorite_numbers.items():

#     all_nums = ", ".join(map(str, numbers))
#     word = "numbers are" if len(numbers) > 1 else "number is"
    
#     print(f"\n{name.title()}'s favorite {word}: {all_nums}.")

# -----------------------------------------------------------

# 6-11
# cities = {
#     "cairo": {
#         "country": "egypt",
#         "population": 10_000_000, # استخدمنا الـ underscore لجعل الرقم مقروءاً
#         "fact": "It is known as the city of a thousand minarets.",
#     },
#     "tokyo": {
#         "country": "japan",
#         "population": 37_000_000,
#         "fact": "It is the most populated metropolitan area in the world.",
#     },
#     "paris": {
#         "country": "france",
#         "population": 2_100_000,
#         "fact": "It is famous for the Eiffel Tower.",
#     },
# }

# for city, info in cities.items():
#     print(f"\nCity: {city.title()}")
    
#     country = info['country'].title()
#     pop = info['population']
#     fact = info['fact']
    
#     print(f"\tCountry: {country}")
#     print(f"\tApproximate population: {pop:,}") # الـ :, تضع فواصل آلاف تلقائياً عند الطباعة
#     print(f"\tFact: {fact}")

