# TRY IT YOURSELF page 155

# # 7-1
# car_type = input("what kind of rental car you would like? : ")
# print(f"Let me see if I can find you a {car_type}.")


# # # 7-2
# number_of_people = input("How many people are in their dinner group? : ")
# number_of_people = int(number_of_people)

# if number_of_people > 8:
#     print("You'll have to wait for a table.")
# else:
#     print("Your table is ready.")


# # 7-3
# message = "choosse a number."
# message += "\nand I'll tell you if it is a multiple of ten or not.: "
# number = int(input(message))

# if number % 10 == 0:
#     print(f"The number {number} is multiply of ten")
# else:
#     print(f"The number {number} isn't a multiple of ten")


# -----------------------------------------------------------


# TRY IT YOURSELF page 161

# # # 7-4
# prompt = "enter a pizza toppings and"
# prompt += "\nenter 'quit' when you finish, please: "

# while True:
#     topping = input(prompt)
#     if topping.lower() == 'quit':
#         break
#     else:
#         print(f"We'll add {topping} to your pizza.")


# # 7-5
# prompt = "\nPlease enter your age to see the ticket price:"
# prompt += "\n(Enter 'quit' when you are finished) "

# while True:
#     age_input = input(prompt)

#     if age_input.lower().startswith('q'):
#         break

#     try:
#         age = int(age_input)
#     except ValueError:
#         print("Please enter a valid number or 'quit' to exit.")
#         continue

#     if age < 0:
#         print("Age cannot be negative! Please enter a real age.")

#     if age < 3:
#         print("Your ticket is free!")
#     elif age <= 12:
#         print("Your ticket cost is $10.")
#     else:
#         print("Your ticket cost is $15.")


# # 7-6  from 7-4
prompt = "enter a pizza toppings and"
prompt += "\nenter 'quit' when you finish, please: "

# # 7-6-1
# while True:
#     topping = input(prompt).lower()
#     if topping == 'quit':
#         break
#     else:
#         print(f"We'll add {topping} to your pizza.")

# # # 7-6-2
# active = True
# while active:
#     topping = input(prompt)
#     if topping.lower() == 'quit':
#         active = False
#     else:
#         print(f"We'll add {topping} to your pizza.")

# # 7-6-3
# topping = ""
# while not topping.lower().startswith("q"):
#     topping = input(prompt)
#     if not topping.lower().startswith("q"):
#         print(f"We'll add {topping} to your pizza.")


# -----------------------------------------------------------

# # TRY IT YOURSELF page 165

# # 7-8 & 7-9
# sandwich_orders = ["tuna", "pastrami", "grilled cheese", "pastrami", "turkey", "roast beef", "pastrami"]
# finished_sandwiches = []

# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")


# print("deli has run out of pastrami")


# while sandwich_orders:
#     being_prepared = sandwich_orders.pop()
#     print(f"I made your {being_prepared} sandwich.")
#     finished_sandwiches.append(being_prepared)


# print("\n**** Finished Sandwiches ****".center(100))
# for sandwich in finished_sandwiches :
#     print(f"- {sandwich.title()}")


# # 7-10
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    # تخزين الإجابة في القاموس
    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == "no":
        polling_active = False
print(responses)

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
