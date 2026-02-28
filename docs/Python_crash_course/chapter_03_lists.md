القوائم (Lists) في بايثون؟

القائمة في بايثون هي هيكل بيانات (Data Structure) يُستخدم لتخزين عدة عناصر داخل متغير واحد.

بمعنى بسيط:
بدل ما تنشئ متغير لكل قيمة، تضعهم كلهم داخل قائمة واحدة.

names = ["Ali", "Omar", "Sara"]

القائمة في بايثون هي حاوية مرتبة وقابلة للتعديل لتخزين مجموعة من القيم داخل متغير واحد.

🔹 خصائص القوائم

1️⃣ مرتبة (Ordered) → لكل عنصر رقم (Index) يبدأ من 0
2️⃣ قابلة للتغيير (Mutable) → يمكن تعديلها بعد إنشائها
3️⃣ تسمح بتكرار القيم
4️⃣ يمكن أن تحتوي على أنواع بيانات مختلفة

🔹 لماذا القوائم مهمة؟

لأنها تُستخدم في:

تخزين البيانات القادمة من المستخدم

التعامل مع قواعد البيانات

إدارة الطلبات في السيرفرات

أي شيء يحتاج تخزين عدة عناصر



| تريد                 | استخدم             |
| -------------------- | ------------------ |
| عنصر واحد في النهاية | `append()`         |
| عنصر في مكان محدد    | `insert(indix,value)`         |
| عدة عناصر            | `extend()` أو `+=` |
| إنشاء قائمة جديدة    | `+`                |


| تريد                  | استخدم                             |
| --------------------- | ---------------------------------- |
| حذف عنصر بموقع        | `pop(index)` أو `del names[index]` |
| حذف آخر عنصر          | `pop()`                            |
| حذف عنصر بالقيمة      | `remove(value)`                    |
| حذف مجموعة من العناصر | `del names[start:end]`             |
| مسح كل العناصر        | `clear()` أو `del names[:]`        |
| حذف القائمة نفسها     | `del names`                        |


ترتيب القوائم 

1️⃣ sort()
ترتيب القائمة نفسها بالمكان (تغير القائمة الأصلية).

numbers = [3,1,4]
numbers.sort()
print(numbers)   # [1, 3, 4]


2️⃣ sorted()
ترتيب نسخة من القائمة دون تغيير الأصلية.

numbers = [3,1,4]
print(sorted(numbers))  # [1, 3, 4]
print(numbers)          # [3, 1, 4]


3️⃣ reverse()
يعكس ترتيب القائمة نفسها (المكان).

numbers = [1,2,3]
numbers.reverse()
print(numbers)   # [3,2,1]


4️⃣ len()
يعطي عدد عناصر القائمة.

numbers = [1,2,3]
print(len(numbers))  # 3




numbers = [4, 1, 7, 3]

# 1️⃣ len
print("Number of elements:", len(numbers))   # 4

# 2️⃣ reverse
numbers.reverse()
print("After reverse:", numbers)            # [3, 7, 1, 4]

# 3️⃣ sort (modifies the list itself)
numbers.sort()
print("After sort:", numbers)               # [1, 3, 4, 7]

# 4️⃣ sorted (returns a new sorted list, original unchanged)
numbers_copy = [4, 1, 7, 3]
print("Sorted copy:", sorted(numbers_copy)) # [1, 3, 4, 7]
print("Original unchanged:", numbers_copy) # [4, 1, 7, 3]


