# # 10-6. Addition
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 + num2

# except ValueError:
#     print("please, enter valid numbers.")

# else:
#     print(result)

# 10-7. Addition Calculator
while True:
    try:
        num1 = input("Enter first number: ")
        if num1.lower() == "q":
            break
        num2 = input("Enter second number: ")
        if num2.lower() == "q":
            break
        else:
            result = int(num1) + int(num2)

    except ValueError:
        print("please, enter valid numbers.")

    else:
        print(result)
