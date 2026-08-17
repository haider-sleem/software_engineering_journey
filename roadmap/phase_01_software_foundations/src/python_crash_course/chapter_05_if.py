# TRY IT YOURSELF page 115
# 5-1 & 5-2

# example : A
# new_arrival = "omar"
# print("Is new_arrival == 'omar'? I predict True.")
# print(new_arrival == "omar")

# print("\nIs new_arrival == 'ahmed'? I predict False.")
# print(new_arrival == "ahmed")

# example : B
# age = 25
# print("Is age > 18? I predict True.")
# print(age > 18)

# print("\nIs age < 10? I predict False.")
# print(age < 10)

# example : C
# name = "Haider"
# print("Is name.lower() == 'haider'? I predict True.")
# print(name.lower() == "haider")

# print("\nIs name == 'haider'? I predict False.")
# print(name == "haider")

# example : D
# users_count = 100
# print("Is users_count != 100? I predict False.")
# print(users_count != 100)

# print("\nIs users_count != 200? I predict True.")
# print(users_count != 200)

# example : E
# age_0 = 22
# age_1 = 18

# print("Is age_0 >= 21 and age_1 >= 21? I predict False.")
# print(age_0 >= 21 and age_1 >= 21)

# print("\nIs age_0 >= 21 or age_1 >= 21? I predict True.")
# print(age_0 >= 21 or age_1 >= 21)

# print("\nIs age_0 > 20 and age_1 < 20? I predict True.")
# print(age_0 > 20 and age_1 < 20)


# example : F
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# print("Is user not in banned_users? I predict True.")
# print(user not in banned_users)

# user_to_check = 'david'
# print("\nIs 'david' in banned_users? I predict True.")
# print(user_to_check in banned_users)

# print("\nIs 'haider' in banned_users? I predict False.")
# print('haider' in banned_users)

# ------------------------------------------
# TRY IT YOURSELF page 122

# # 5-3
# alien_color = 'green'

# if alien_color == 'green':
#     print("You just earned 5 points!") # نسخة ناجحة


# alien_color = 'yellow'

# if alien_color == 'green':
#     print("You just earned 5 points!") # نسخة فاشلة


# # 5-4
# alien_color = 'green'

# if alien_color == "green":
#     print("the player just earned 5 points for shooting the alien.")
# else :
#     print("the player just earned 10 points.")


# # 5-5
# alien_color = "green" # "yellow" or "red"

# if alien_color == "green":
#     print("the player earned 5 points.")
# elif alien_color == "yellow":
#     print("the player earned 10 points.")
# else:
#     print("the player earned 15 points.")


# # 5-6
# age = 41

# if age < 2:
#     person = "a baby"
# elif age < 4:
#     person = "a toddler"
# elif age < 13:
#     person = "a kid"
# elif age < 20:
#     person = "a teenager"
# elif age < 65:
#     person = "an adult"
# else:
#     person = "an elder"

# print(f"The person is {person}.")

# 5-7
# favorite_fruits = ["banana", "apple", "mango"]

# if "banana" in favorite_fruits:
#     print("You really like bananas!")

# if "apple" in favorite_fruits:
#     print("You really like apples!")

# if "mango" in favorite_fruits:
#     print("You really like mangoes!")

# if "orange" in favorite_fruits:
#     print("You really like oranges!")

# if "strawberry" in favorite_fruits:
#     print("You really like strawberries!")


# --------------------------------------------

# TRY IT YOURSELF page 126

# 5-8
# user_names = ["admin","ali","ahmed","omar","khaled"]
# for user_name in user_names:
#     if user_name.lower() == "admin":
#         print(f"Hello {user_name.capitalize()}, would you like to see a status report?")
#     else:
#         print(f"Hello {user_name.capitalize()}, thank you for logging in again.")


# # 5-9
# user_names = []
# if user_names:
#     for user_name in user_names:
#         if user_name.lower() == "admin":
#             print(f"Hello {user_name.capitalize()}, would you like to see a status report?")
#         else:
#             print(f"Hello {user_name.capitalize()}, thank you for logging in again.")
# else:
#     print("We need to find some users!")


# 5-10 تم تحويل التمرين لدالة لسهولة الإختبار


def is_username_available(new_user, current_users):
    current_users_lower = [user.lower() for user in current_users]
    if new_user.lower() in current_users_lower:
        return False  # يعني الاسم محجوز
    else:
        return True  # يعني الاسم متاح


current_users = ["yasser", "adel", "hytham", "alia", "tamara"]
new_users = ["khaled", "marawan", "adel", "alia", "tamara"]

for user in new_users:
    if is_username_available(user, current_users):
        print(f"The username '{user}' is available.")
    else:
        print(f"The person '{user}' will need to enter a new username.")

# # 5-11
# ordinal_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in ordinal_Numbers:
#     if num == 1:
#         print(f"{num}st")
#     elif num == 2:
#         print(f"{num}nd")
#     elif num == 3:
#         print(f"{num}rd")
#     else:
#         print(f"{num}th")

# -----------------------------------------
