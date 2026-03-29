# Problem #3: Winning Team (DMOJ problem ccc19j1.) page 58

# طريقة حل المسألة في الكتاب أنظر ملف راجع ملف إم دي للطريقة الإحترافية و تحليلها

# apple_three = int(input())
# apple_two = int(input())
# apple_one = int(input())
# banana_three = int(input())
# banana_two = int(input())
# banana_one = int(input())
# apple_total = apple_three * 3 + apple_two * 2 + apple_one
# banana_total = banana_three * 3 + banana_two * 2 + banana_one
# if apple_total < banana_total:
#     print("B")
# elif apple_total > banana_total:
#     print("A")
# else:
#     print("T")


# ------------ حل تمرين مشابه بطريقة الدوال -------------

# def quality_delivery_of_orders(fast_delivery, standard_delivery, slow_delivery):

#     return (fast_delivery * 10) + (standard_delivery * 5) + (slow_delivery * 1 )


# def numbers_of_orders(the_employee_number):

#     print()
#     print("=" * 30)
#     print()
#     print(f"--- Enter the number of orders for {the_employee_number} ---")

#     fast_delivery = int(input("Enter the number of fast delivery orders : "))
#     standard_delivery = int(input("Enter the number of standard delivery orders : "))
#     slow_delivery = int(input("Enter the number of slow delivery orders : "))

#     return quality_delivery_of_orders(fast_delivery, standard_delivery, slow_delivery)


# delivery_one = numbers_of_orders("the first employee")
# delivery_two = numbers_of_orders("the second employee")

# print("=" * 30)
# print()
# print(f"The result is ; the first employee {delivery_one} | the second employee {delivery_two}")
# if delivery_one > delivery_two:
#     print("\nThe most efficient delivery is the first employee ")
# elif delivery_one < delivery_two:
#     print("\nThe most efficient delivery is the second employee")
# else:
#     print("\nThe two employees are equal")




