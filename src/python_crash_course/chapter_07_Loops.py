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


# # 7-6  page 161
