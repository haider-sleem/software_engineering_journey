# # ============================================================
# # Chapter 2 – Strings & Numbers
# # Python Crash Course
# # ============================================================


# # ============================================================
# # 1. Updating Variables
# # ============================================================

# message = "Hello Python world!"  # Initial message
# print(message)

# message = "Hello Python crash course world!"  # Updated message
# print(message)


# # ============================================================
# # 2. String Formatting Methods
# # ============================================================

# name = "ada lovelace"

# print(name.title())  # Capitalizes first letter of each word
# print(name.upper())  # Converts all letters to uppercase
# print(name.lower())  # Converts all letters to lowercase


# # ============================================================
# # 3. Concatenating Strings
# # ============================================================

# first_name = "ada"
# last_name = "lovelace"

# full_name = first_name + " " + last_name  # Space important between first and last name
# print(full_name)

# message = "Hello, " + full_name.title() + "!"  # Greeting message
# print(message)

def get_full_name(first, last):
    """هذه الدالة تأخذ الاسم الأول والأخير وتعيد الاسم الكامل منسقاً"""
    full_name = first + ' ' + last 
    return full_name.title()


# # ============================================================
# # 4. Whitespace and Formatting
# # ============================================================

# print("python")        # Normal print
# print("\tpython")      # Tab adds indentation

# print("Languages:\nPython\nC\nJavaScript")  # New line after each language

# favorite_language = " python "
# print(favorite_language.rstrip())  # Remove trailing spaces
# print(favorite_language.lstrip())  # Remove leading spaces
# print(favorite_language.strip())   # Remove both leading and trailing spaces

# favorite_language = favorite_language.strip()  # Permanently update variable


# # ============================================================
# # 5. Apostrophes in Strings
# # ============================================================

# message = "One of Python's strengths is its diverse community."  # Apostrophe in string
# print(message)


# # ============================================================
# # 6. Removing Prefixes and Suffixes
# # ============================================================

# url = "http://example.com/"

# clean = url.removeprefix("http://")  # Remove prefix
# clean = clean.removesuffix(".com/")  # Remove suffix
# print(clean)

# clean = url.removeprefix("http://").removesuffix(".com/")  # One-liner
# print(clean)


# # ============================================================
# # 7. Working with File Names (splitext)
# # ============================================================

# import os

# filename = "python_notes.txt"
# name_without_extension = os.path.splitext(filename)[0]  # Get filename without extension

# print(name_without_extension)


# # ============================================================
# # 8. Numbers – Underscore for Large Numbers
# # ============================================================

# big_number = 14_000_000_000  # Underscores improve readability
# print(big_number)   # 14000000000


# # ============================================================
# # 9. Multiple Assignment (Numbers)
# # ============================================================

# x, y, z = 0, 0, 0  # Assign same value to multiple variables
# print(x, y, z)


# # ============================================================
# # 10. Multiple Assignment (Strings)
# # ============================================================

# first_name, last_name, country = "Haider", "Sleem", "Egypt"

# print("First_name:", first_name)
# print("Last_name:", last_name)
# print("Country:", country)


# # ============================================================
# # 11. Constants
# # ============================================================

# MAX_CONNECTIONS = 5000  # Treat as constant
# print(MAX_CONNECTIONS)


# # ============================================================
# # 12. Try It Yourself – Exercises
# # ============================================================

# print(5 + 3)        # Addition
# print(16 / 2)       # Division always returns float
# print(2 * 4)        # Multiplication
# print(10 - 2)       # Subtraction

# my_favorite_number = 9
# print("My favorite number is:", my_favorite_number)  # Display favorite number
