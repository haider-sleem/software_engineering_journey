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

####### 1. DMOJ problem ccc06j1, Canadian Calorie Counting ###########


# ------------------ الحل ب الجملة الشرطية فقط -----------------

# burger_choices = int(input())
# if burger_choices == 1:
#     burger_calories = 461
# elif burger_choices == 2:
#     burger_calories = 431
# elif burger_choices == 3:
#     burger_calories = 420
# else:
#     burger_calories = 0


# side_order_choices = int(input())
# if side_order_choices == 1:
#     side_order_calories = 100
# elif side_order_choices == 2:
#     side_order_calories = 57
# elif side_order_choices == 3:
#     side_order_calories = 70
# else:
#     side_order_calories = 0

# drink_choices = int(input())
# if drink_choices == 1:
#     drink_calories = 130
# elif drink_choices == 2:
#     drink_calories = 160
# elif drink_choices == 3:
#     drink_calories = 118
# else:
#     drink_calories = 0


# dessert_choices = int(input())
# if dessert_choices == 1:
#     dessert_calories = 167
# elif dessert_choices == 2:
#     dessert_calories = 266
# elif dessert_choices == 3:
#     dessert_calories = 75
# else:
#     dessert_calories = 0

# total_calories = ( burger_calories + drink_calories
# + side_order_calories + dessert_calories )

# print(f"Your total Calorie count is {total_calories}.")


# ------------------------- الحل بالدوال------------------------

# def Calorie_count(burger_calories, drink_calories, side_order_calories, dessert_calories):
#     return (burger_calories + drink_calories + side_order_calories + dessert_calories)


# def calculate_total_calories():

#     burger_choices = int(input())
#     drink_choices = int(input())
#     side_order_choices = int(input())
#     dessert_choices = int(input())


#     if burger_choices == 1:
#         burger_calories = 461
#     elif burger_choices == 2:
#         burger_calories = 431
#     elif burger_choices == 3:
#         burger_calories = 420
#     else:
#         burger_calories = 0


#     if side_order_choices == 1:
#         side_order_calories = 100
#     elif side_order_choices == 2:
#         side_order_calories = 57
#     elif side_order_choices == 3:
#         side_order_calories = 70
#     else:
#         side_order_calories = 0


#     if drink_choices == 1:
#         drink_calories = 130
#     elif drink_choices == 2:
#         drink_calories = 160
#     elif drink_choices == 3:
#         drink_calories = 118
#     else:
#         drink_calories = 0


#     if dessert_choices == 1:
#         dessert_calories = 167
#     elif dessert_choices == 2:
#         dessert_calories = 266
#     elif dessert_choices == 3:
#         dessert_calories = 75
#     else:
#         dessert_calories = 0

#     total = Calorie_count(burger_calories,  side_order_calories,drink_calories, dessert_calories)
#     print(f"Your total Calorie count is {total}.")

# calculate_total_calories():


# ---------------------- الحل بإستخدام القواميس --------------------------


# # 1. تخزين البيانات في قواميس (مفاتيح وقيم)
# # الميزة هنا أننا نحدد "الاختيار" و "سعراته" بوضوح

# burgers = {1: 461, 2: 431, 3: 420, 4: 0}
# sides =   {1: 100, 2: 57, 3: 70, 4: 0}
# drinks =  {1: 130, 2: 160, 3: 118, 4: 0}
# desserts = {1: 167, 2: 266, 3: 75, 4: 0}

# # 2. استقبال الاختيارات
# b = int(input())
# s = int(input())
# d = int(input())
# ds = int(input())

# # 3. استخدام دالة .get(key, default)
# # هذه الدالة تبحث عن الرقم، وإذا لم تجده (مثلاً أدخل 5) تعطي قيمة 0 تلقائياً ولا ينهار البرنامج
# total = (burgers.get(b, 0) +
#          sides.get(s, 0) +
#          drinks.get(d, 0) +
#          desserts.get(ds, 0))

# print(f"Your total Calorie count is {total}.")

# -------------------------  حل إحترافي بالدوال-تتميز بال"المسؤولية الواحدة" (Single Responsibility Principle). لكل دالة-------------------


# def get_calories(menu, item_name):
#     try:
#         user_input = input(f"Enter your choice for {item_name} (1-4): ")
#         choice = int(user_input)
#         return menu[choice - 1]
#     except (IndexError, ValueError):
#         return 0


# def main():
#     burgers  = [461, 431, 420, 0]
#     sides    = [100, 57, 70, 0]
#     drinks   = [130, 160, 118, 0]
#     desserts = [167, 266, 75, 0]

#     total = (
#         get_calories(burgers, "burger") +
#         get_calories(sides, "side") +
#         get_calories(drinks, "drink") +
#         get_calories(desserts, "dessert")
#     )

#     print(f"\nYour total Calorie count is {total}.")


# main()


# ###############################################################

# # 2. DMOJ problem ccc15j1, Special Day page 81

# month_input = int(input())
# day_input = int(input())

# if month_input < 2:
#     print("Before")
# elif month_input > 2:
#     print("After")
# else:
#     if day_input < 18:
#         print("Before")
#     elif day_input > 18:
#         print("After")
#     else:
#         print("Special")

# ---------------  حل تاني للمسألة السابقة  بإفتراض  ------
# أخطاء نوع البيانات (Data Type Errors)
# أخطاء النطاق والقيم (Range & Logic Errors)


# year = 2015
# while True: # إدخال الشهر
#     val1 = input("Enter Month (1-12): ").strip()

#     if val1.isdigit():
#         month_input = int(val1)
#         if 1 <= month_input <= 12:
#             break
#         else:
#             print("Error: Number must be between 1 and 12")
#     else:
#         print("Error: Please enter digits only (0-9)")

# while True: # إدخال اليوم

#     val2 = input("Enter Day (1-31): ").strip()

#     if val2.isdigit():
#         day_input = int(val2)

#         # تحديد max_days حسب الشهر
#         if month_input in (1, 3, 5, 7, 8, 10, 12):
#             max_days = 31
#         elif month_input in (4, 6, 9, 11):
#             max_days = 30
#         elif month_input == 2:
#             if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#                 max_days = 29
#                 print("Info: Leap year detected (29 days in February)")
#             else:
#                 max_days = 28
#         else:
#             print("Error: Invalid day")  # للأمان بس
#             continue

#         # ✅ شيك واحد على اليوم في الآخر
#         if 1 <= day_input <= max_days:
#             break
#         else:
#             print(f"Error: This month has {max_days} days,from (1-{max_days})")

#     else:
#         print("Error: Please enter digits only (0-9)")

# print(f"\n✅ Valid date: {month_input}/{day_input}/{year}")

# # منطق المسألة الأساسي بعد التأكد من صحة المدخلات
# date_input = (month_input, day_input)
# special_date = (2, 18)

# if date_input < special_date:
#     print("Before")
# elif date_input > special_date:
#     print("After")
# else:
#     print("Special")


# ############## 3. DMOJ problem ccc15j2, Happy or Sad page 81 ########

# message = input("")

# happy_count = message.count(":-)")
# sad_count = message.count(":-(")

# if happy_count > sad_count:
#     print("happy")
# elif sad_count > happy_count:
#     print("sad")
# elif happy_count == 0:
#     print("none")
# else:
#     print("unsure")


# ######### 4. DMOJ problem dmopc16c1p0, C.C. and Cheese-kun page 81 ########

# # قراءة المدخلات
# width = int(input())
# cheese = int(input())

# # تحديد مستوى الرضا
# if width == 3 and cheese >= 95:
#     satisfaction = "absolutely"
# elif width == 1 and cheese <= 50:
#     satisfaction = "fairly"
# else:
#     satisfaction = "very"

# # طباعة الناتج بنفس التنسيق المطلوب
# print(f"C.C. is {satisfaction} satisfied with her pizza.")


# ######### 5. DMOJ problem ccc07j1, Who is in the Middle page 81 ########

# # قراءة الأوزان الثلاثة
# weight1 = int(input())
# weight2 = int(input())
# weight3 = int(input())

# # إيجاد الوزن الأوسط
# # طريقة 1: استخدام دالة sorted
# weights = sorted([weight1, weight2, weight3])
# print(weights[1])

# أو بطريقة أخرى بدون sorted:

# middle = weight1 + weight2 + weight3 - max(weight1, weight2, weight3) - min(weight1, weight2, weight3)
# print(middle)
