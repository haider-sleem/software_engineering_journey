# # TRY IT YOURSELF page 74

# 3-1
# names = ['Elbaz','Essa','Nozha','Hima']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# 3-2
# names = ['Baz','Essa','Nozha','Hima']
# message1 = f'Alsalam Alukum, how are you {names[0].title()} ?'
# print(message1)
# message2 = f'Alsalam Alukum, how are you {names[1].title()} ?'
# print(message2)
# # and so on

# 3-3
# cars = ['Vovlvo','Toyouta','Geep']
# message = f'I would like to have a {cars[2]} one day.'
# print(message)

# # 3-4
# Guest_List = ['Basel','Baher','Ali']
# print(f'{ Guest_List[0].title()},I would like to have dinner together.')  # and so on

# 3-5
# Guest_List = ['Basel','Baher','Ali','Othman']
# print(f"But {Guest_List[3]},can't come to the dinner party.")
# Guest_List[3] = "Alia"
# print(f'{ Guest_List[3].title()},I would like to have dinner together.')    # and so on

# 3-6
Guest_List = ["Basel", "Baher", "Ali", "Alia"]
print("Good news! I found a bigger dinner table.")
Guest_List.insert(0, "Nana")
Guest_List.insert(1, "Mama")
Guest_List.append("Tamara")
print(Guest_List)
print(
    f"Hello {Guest_List[0]}, you are invited to have dinner with us tomorrow."
)  # and so on
for gust in Guest_List:
    print(f"Hello {gust}, you are invited to have dinner with us tomorrow.")

# 3-7
# print(
#     "Sorry , our new dinner table won't arrive in time,so I can invite only two people for the dinner."
# )
# Guest_List = ["Nana", "Mama", "Basel", "Baher", "Ali", "Alia", "Tamara"]
# canceled_invitayion = Guest_List.pop()  # هيمسح الأخير تلقائي
# canceled_invitayion2 = Guest_List.pop(1)  # هيمسح إل متحدد
# print(f"Sorry,{canceled_invitayion} and {canceled_invitayion2} I can’t invite you to dinner.")
# print(f"{Guest_List[0]}, you’re still invited.")
# del Guest_List[:]       # Guest_List.clear()
# print(Guest_List)


# # TRY IT YOURSELF page 83

# # 3-8
# places_to_visit = ["Mecca", "Medina", "East Asia", "Switzerland", "Russia"]
# print(places_to_visit)
# print(sorted(places_to_visit))
# print(places_to_visit)
# print(sorted(places_to_visit,reverse=True))
# print(places_to_visit)
# places_to_visit.reverse() #لو طبعتها على طول هترجع None
# print(places_to_visit)
# places_to_visit.reverse()
# print(places_to_visit)
# places_to_visit.sort()
# print(places_to_visit)
# places_to_visit.reverse()
# print(places_to_visit)


# # 3-9
# Guest_List = ["Nana", "Mama", "Basel", "Baher", "Ali", "Alia", "Tamara"]
# print(len(Guest_List))


# # 3-10
# # إنشاء القائمة
# countries = ["Japan", "Brazil", "Egypt", "Canada"]

# # append() → إضافة عنصر
# countries.append("Switzerland")

# # insert() → إضافة عنصر في موقع محدد
# countries.insert(2, "Russia")

# # remove() → حذف عنصر بالقيمة
# countries.remove("Brazil")

# # pop() → حذف عنصر بموقع محدد وإرجاعه
# removed = countries.pop(3)
# print("Removed country:", removed)

# # sort() → ترتيب أبجدي
# countries.sort()

# # reverse() → عكس القائمة
# countries.reverse()

# # len() → عدد العناصر
# print("Number of countries:", len(countries))

# # sorted() → نسخة مرتبة دون تغيير الأصلية
# print("Alphabetical copy:", sorted(countries))

# # clear() → مسح كل العناصر
# countries.clear()
# print("After clear():", countries)


