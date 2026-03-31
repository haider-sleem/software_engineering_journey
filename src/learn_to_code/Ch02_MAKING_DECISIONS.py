# Problem #3: Winning Team (DMOJ problem ccc19j1.) page 58

# طريقة حل المسألة في الكتاب راجع ملف إم دي للطريقة الإحترافية و تحليلها

# # Entering results
# apple_three = int(input())
# apple_two = int(input())
# apple_one = int(input())
# banana_three = int(input())
# banana_two = int(input())
# banana_one = int(input())

# # Compilation of results
# apple_total = apple_three * 3 + apple_two * 2 + apple_one
# banana_total = banana_three * 3 + banana_two * 2 + banana_one

# # Determine the winner
# if apple_total < banana_total:
#     print("B")
# elif apple_total > banana_total:
#     print("A")
# else:
#     print("T")


# ------------ حل تمرين مشابه بطريقة الدوال -------------

# # إنشاء دالة منفصلة للمعالجة أولا
# def quality_delivery_of_orders(fast_delivery, standard_delivery, slow_delivery):

#     return (fast_delivery * 10) + (standard_delivery * 5) + (slow_delivery * 1 )

# # ثم إنشاء دالة إدخال للبيانات التي سيتم معالجتها بالدالة السابقة
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

# ----------------------------------------------------

# # Problem #4: Telemarketer or not ( DMOJ problem ccc18j1.) page 72

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())

# if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
#     print("ignore")
# else:
#     print("answer")

"""
# صياغة إحترافية أكثر لنفس الإسلوب

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if num1 in (8, 9) and num4 in (8, 9) and num2 == num3:
    print('ignore')
else:
    print('answer')
"""

"""
حل آخر إحترافي أكثر 

# Read all 4 inputs at once using a list comprehension
# This is faster and cleaner than 4 separate lines

tele = [int(input()) for _ in range(4)] # تستخدم ( _ )كتعبير عن متغير لا حاجة لتسميته عندما لن يستخدم

# Professional logic check
is_telemarketer = (
    tele[0] in (8, 9) and 
    tele[3] in (8, 9) and 
    tele[1] == tele[2]
)

# Output based on the result
print("ignore" if is_telemarketer else "answer")

"""

"""
The best practice solution on the  DMOJ site 

telemarketer = True
for i in range(4):
    number = int(input())
    if telemarketer:
        if i == 0 or i == 3:
            if number == 8 or number == 9:
                telemarketer = True
            else:
                telemarketer = False
        elif i == 1:
            secondDigit = number
        elif i == 2:
            if number == secondDigit:
                telemarketer = True
            else:
                telemarketer = False
if telemarketer:
    print('ignore')
else:
    print('answer')


المميزات (الاحترافية التقنية) للكود ثم عيوبه :

كفاءة الذاكرة (Memory Efficiency): تخزين رقم واحد فقط كل مرة.

الخروج المبكر (Early Exit): إيقاف الفحص فور فشل الشرط.

أداء عالٍ (High Performance): مثالي لمعالجة ملايين البيانات الضخمة.

توفير العمليات (Low Operations): تقليل مقارنات المعالج غير الضرورية.

العيوب (منظور الكود النظيف):

تعقيد القراءة (High Complexity): كثرة الشروط المتداخلة تُشتت المبرمج.

صعوبة الصيانة (Hard Maintainability): تعديل أي شرط يتطلب حذراً شديداً.

عدم الاختصار (Too Verbose): كتابة أسطر كثيرة لمهمة بسيطة.

عرضة للأخطاء (Error Prone): تداخل الـ if يسهل نسيان حالة.



"""



# -------------  Chapter 02 Exercises page 81 -------
