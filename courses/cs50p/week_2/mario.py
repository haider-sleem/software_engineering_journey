print("#")
print("#")
print("#")

print("*" * 10)
##########################################################

# # Update: Instead of repeating print statements manually, use a for loop to print the column dynamically.

# for _ in range(3):
#     print("#")

# print("*" * 10)
# ##########################################################

# # Update: Instead of hard-coding the number 3, use a function parameter so the column height can be changed easily.


# def print_column(height):
#     for _ in range(height):
#         print("#")


# def main():
#     print_column(3)


# main()

# print("*" * 10)
# ##########################################################

# # Update: The function's internal implementation can be changed without changing how main() uses print_column().


# def print_column(height):
#     print("#\n" * height, end="")


# def main():
#     print_column(3)


# main()

# print("*" * 10)
# ##########################################################

# # Update: Instead of printing a vertical column, create a reusable function for printing a horizontal row.


# def print_row(width):
#     print("?" * width)


# def main():
#     print_row(4)


# main()

# print("*" * 10)
# ##########################################################

# # Update: A square needs both rows and columns, so use a nested loop to print multiple rows and multiple bricks per row.


# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")
#         print()


# def main():
#     print_square(3)


# main()

# print("*" * 10)
# ##########################################################

# # Update: The inner loop can be replaced with string multiplication, making print_square() shorter while producing the same result.


# def print_square(size):
#     for i in range(size):
#         print("#" * size)


# def main():
#     print_square(3)


# main()

# print("*" * 10)
# ##########################################################

# # Update: Use a separate print_row() function to abstract the responsibility of printing one row from print_square().


# def print_row(width):
#     print("#" * width)


# def print_square(size):
#     for i in range(size):
#         print_row(size)


# def main():
#     print_square(3)


# main()

# print("*" * 10)
# ##########################################################
