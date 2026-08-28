# # TRY IT YOURSELF page 200


# # 9-1. Restaurant
# class Restaurant:
#     """Represent a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize name and type attributes."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """ prints restaurant name and type """
#         print(
#             f"{'Restaurant':<12}: {self.restaurant_name}\n"
#             f"{'Cuisine':<12}: {self.cuisine_type}"
#         )

#     def open_restaurant(self):
#         """ prints a message indicating that the restaurant is open. """
#         print(f"{self.restaurant_name} is open.")


# restaurant = Restaurant("Zoom", "Egyptian")

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# # 9-2. Three Restaurants

# restaurant1 = Restaurant("sham", "syrian")
# restaurant2 = Restaurant("tika", "turksih")
# restaurant3 = Restaurant("kibdaky", "Egyptian")

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()


# # 9-3. Users
# class User:
#     """ define the users first and last name."""

#     def __init__(self, first_name,  last_name, age, job):
#         """Inintializes users attributes."""
#         self.first_name    = first_name
#         self.last_name     = last_name
#         self.age           = age
#         self.job           = job

#     def  describe_user(self):
#         """ describes all the user available details."""

#         print(f"The user name is {self.first_name} {self.last_name}, he is {self.age} years old, and his/her job is {self.job}.")

#     def  greet_user(self):
#         """ prints personal greetting to the user."""

#         print(f"Hello, {self.first_name} {self.last_name}")

# ali = User("Ali", "sleem", 20, "student" )

# ali.describe_user()
# ali.greet_user


# # TRY IT YOURSELF page 204 & 205

# # 9-4. Number Served
# class Restaurant:
#     """Represent a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize name and type attributes."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """ prints restaurant name and type """
#         print(
#             f"{'Restaurant':<12}: {self.restaurant_name}\n"
#             f"{'Cuisine':<12}: {self.cuisine_type}"
#         )

#     def open_restaurant(self):
#         """ prints a message indicating that the restaurant is open. """
#         print(f"{self.restaurant_name} is open.")

#     def set_number_served(self, number_served):
#         """  set the number of customers that have been served. """
#         self.number_served = number_served

#     def increment_number_served(self, increment):
#         """ increment the number of customers who’ve been served. """
#         self.number_served += increment

# restaurant = Restaurant("Alhara", "Egyptian")
# print(restaurant.number_served)
# restaurant.number_served = 10
# print(restaurant.number_served)

# restaurant.set_number_served(15)
# print(restaurant.number_served)

# restaurant.increment_number_served(5)
# print(restaurant.number_served)


# # # 9-5. Login Attempts
# class User:
#     """ define the users first and last name."""

#     def __init__(self, first_name,  last_name, age, job, login_attempts=0):
#         """Inintializes users attributes."""
#         self.first_name     = first_name
#         self.last_name      = last_name
#         self.age            = age
#         self.job            = job
#         self.login_attempts = login_attempts

#     def  describe_user(self):
#         """ describes all the user available details."""

#         print(f"The user name is {self.first_name} {self.last_name}, "
#               f"he is {self.age} years old, "
#               f"and his/her job is {self.job}."
#             )

#     def  greet_user(self):
#         """ prints personal greetting to the user."""

#         print(f"Hello, {self.first_name} {self.last_name}")

#     def increment_login_attempts(self):
#         """ increments the value of login attempts by 1 """
#         self.login_attempts += 1


#     def reset_login_attempts(self):
#         """ resets login attempts to 0 """
#         self.login_attempts = 0


# ali = User(input("Enter the user first name "),
#            input("Enter the user last name "),
#            input("Enter the user age "),
#            input("Enter the user job "),
#            )

# ali.describe_user()
# ali.greet_user()
# ali.increment_login_attempts()
# ali.increment_login_attempts()
# ali.increment_login_attempts()
# ali.increment_login_attempts()
# ali.increment_login_attempts()
# print(ali.login_attempts)
# ali.reset_login_attempts()
# print(ali.login_attempts)


# TRY IT YOURSELF page 211

# # 9-6. Ice Cream Stand
# class Restaurant:
#     """Represent a restaurant."""

#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize name and cuisine type."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """ prints restaurant name and type """
#         print(
#             f"{'Restaurant':<21}: {self.restaurant_name}\n"
#             f"{'Cuisine':<21}: {self.cuisine_type}"
#         )

#     def open_restaurant(self):
#         """ prints a message indicating that the restaurant is open. """
#         print(f"{self.restaurant_name} is open.")


# class IceCreamStand(Restaurant):
#     """ ice cream stand is a specific kind of restaurant. """
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         """ Initialize the restaurant and its available ice cream flavors. """
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors

#     def display_flavors(self):
#         print(f"{'Available flavors are':<21}: {', '.join(self.flavors)}")

# restaurant1 = IceCreamStand("rolls", "dessert", ["mango", "chocolate", "vanilla"])
# print(restaurant1.restaurant_name)
# restaurant1.describe_restaurant()
# restaurant1.display_flavors()


# # # 9-7. Admin
# class User:
#     """ define the users first and last name."""

#     def __init__(self, first_name,  last_name, age, job):
#         """Inintializes users first_name,  last_name, age and job."""
#         self.first_name    = first_name
#         self.last_name     = last_name
#         self.age           = age
#         self.job           = job

#     def  describe_user(self):
#         """ describes all the user available details."""

#         print(f"The user name is {self.first_name} {self.last_name}, "
#               f"he is {self.age} years old, "
#               f"and his/her job is {self.job}."
#               )

#     def  greet_user(self):
#         """ prints personal greetting to the user."""

#         print(f"Hello, {self.first_name} {self.last_name}")

# class Admin(User):
#     """ shows a special kind of user."""

#     def __init__(self, first_name,  last_name, age, job, privileges):
#         super().__init__(first_name,  last_name, age, job)
#         self.privileges = privileges

#     def show_privileges(self):
#         """ shows the privileges of the admin. """
#         print(f"The Admin privileges are: {', '.join(self.privileges[:-1])} and {self.privileges[-1]}.")

# admin1 = Admin("Yasser", "EL Adl", 40, "manager", ["can add post", "can delete post", "can ban user"])
# admin1.show_privileges()


# # 9-8. Privileges

# class User:
#     """ define the users first and last name."""

#     def __init__(self, first_name,  last_name, age, job):
#         """Inintializes users first_name,  last_name, age and job."""
#         self.first_name    = first_name
#         self.last_name     = last_name
#         self.age           = age
#         self.job           = job

#     def  describe_user(self):
#         """ describes all the user available details."""

#         print(f"The user name is {self.first_name} {self.last_name}, "
#               f"he is {self.age} years old, "
#               f"and his/her job is {self.job}."
#               )

#     def  greet_user(self):
#         """ prints personal greetting to the user."""

#         print(f"Hello, {self.first_name} {self.last_name}")

# class Privileges:
#     """ shows the privileges of an admin. """
#     def __init__(self, privileges):
#         """ Inintializes admins privileges as a list. """
#         self.privileges = privileges

#     def show_privileges(self):
#         """ shows the privileges of the admin. """
#         if len(self.privileges) > 1:
#             print(f"The Admin privileges are: {', '.join(self.privileges[:-1])} and {self.privileges[-1]}.")
#         elif len(self.privileges) == 1:
#             print(f"The Admin privilege is: {''.join(self.privileges)}.")
#         else:
#             print("No privileges to show.")


# class Admin(User):
#     """ shows a special kind of user."""

#     def __init__(self, first_name,  last_name, age, job, privileges):
#         super().__init__(first_name,  last_name, age, job)
#         self.privileges = Privileges(privileges)


# admin1 = Admin("Yasser", "EL Adl", 40, "manager", ["can add posts", "can delete posts", "can ban users"])
# admin1.privileges.show_privileges()


# # 9-9. Battery Upgrade
# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles


# class Battery:
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=40):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225

#         print(f"This car can go about {range} miles on a full charge.")

#     def upgrade_battery(self):
#         """checks the battery size and set the capacity to 65 if it isn’t already."""
#         if self.battery_size != 65:
#             self.battery_size = 65


# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()


# my_leaf = ElectricCar("nissan", "leaf", 2024)

# my_leaf.battery.get_range()
# my_leaf.battery.upgrade_battery()
# my_leaf.battery.get_range()


# TRY IT YOURSELF page 217

# 9-10. Imported Restaurant:
# Note: This exercise involves modules and multiple files.
# The code has been moved to its own directory: 'chapter_09-10_exercise'


# 9-11. Imported Admin:
# Note: This exercise involves storing User, Privileges, and Admin in a single module.
# The code has been moved to its own directory: 'chapter_09-11_exercise'


# 9-12. Multiple Modules:
# Note: This exercise involves splitting classes across multiple modules (User in one, Admin/Privileges in another).
# The code has been moved to its own directory: 'chapter_09-12_exercise'


#  TRY IT YOURSELF page 218

# # 9-13. Dice
# from random import randint


# class Die:
#     """Represent a die with a configurable number of sides."""

#     def __init__(self, sides=6):
#         """Initialize the class attributes."""
#         self.sides = sides

#     def roll_die(self):
#         """Print a random number between 1 and the number of sides."""
#         print(randint(1, self.sides))


# die6 = Die()
# for _ in range(10):
#     die6.roll_die()

# die10 = Die(10)
# for _ in range(10):
#     die10.roll_die()

# die20 = Die(20)
# for _ in range(10):
#     die20.roll_die()


# # # 9-14. Lottery
# from random import choice

# mixed_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]


# class Lottery:
#     """Represent a lottery ticket generator."""

#     def __init__(self, mixed_list):
#         """Initialize the class attributes."""
#         self.mixed_list = mixed_list

#     def randomly_ticket(self):
#         """Choices a ticket randomly."""
#         return choice(self.mixed_list)


# ticket = Lottery(mixed_list)
# code = ""
# for _ in range(4):
#     code += str(ticket.randomly_ticket())

# print(f"Any ticket matching these 4 numbers or letters: {code} wins a prize.")


# # 9-15. Lottery Analysis
# count = 0
# winning_code = ""
# while winning_code != code:
#     winning_code = ""
#     for _ in range(4):
#         winning_code += str(ticket.randomly_ticket())
#     count += 1

#     if winning_code == code:
#         break


# print(f"The loop had to run {count} to give me a winning ticket.")


# 9-16. Python Module of the Week
"""
9-16. Python Module of the Week: One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
https://pymotw.com and look at the table of contents. Find a module that looks
interesting to you and read about it, perhaps starting with the random module
"""
