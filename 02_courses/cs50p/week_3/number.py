# try:
#     x = int(input("What is x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"X is {x}.")

###################################

# while True:
#     try:
#         x = int(input("What is x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         print(f"X is {x}.")
#         break

# ###################################
# def main():
#     x = get_int()
#     print(f"X is {x}.")


# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x

# main()


# ###################################
# def main():
#     x = get_int()
#     print(f"X is {x}.")


# def get_int():
#     while True:
#         try:
#             return int(input("What is x? "))
#         except ValueError:
#             pass

# main()

###################################
def main():
    x = get_int("What is x? ")
    y = get_int("What is y? ")

    print(f"total is {x + y}.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
