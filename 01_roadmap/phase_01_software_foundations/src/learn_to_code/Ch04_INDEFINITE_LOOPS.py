# Chapter Exercises page 142


# # 1. DMOJ problem ccc20j2, Epidemiology
# p = int(input())
# n = int(input())
# r = int(input())

# total_infected = n
# last_day_infected = n

# days = 0

# while total_infected <= p:
#     last_day_infected = last_day_infected * r
#     total_infected += last_day_infected
#     days += 1
# print(days)


# # 2. DMOJ problem coci08c1p2, Ptice
# question_n = int(input())
# correct_answers = input()

# adrian_score = 0
# adrian_pattern = "ABC"

# bruno_score = 0
# bruno_pattern = "BABC"

# goran_score = 0
# goran_pattern = "CCAABB"

# for i in range(len(correct_answers)):
#     if correct_answers[i] == adrian_pattern[i % 3]:
#         adrian_score += 1

#     if correct_answers[i] == bruno_pattern[i % 4]:
#         bruno_score += 1

#     if correct_answers[i] == goran_pattern[i % 6]:
#         goran_score += 1

# highest_score = max(adrian_score, bruno_score, goran_score)

# print(highest_score)

# if adrian_score == highest_score:
#     print("Adrian")

# if bruno_score == highest_score:
#     print("Bruno")

# if goran_score == highest_score:
#     print("Goran")
"""
Note: Handling Patterns in Logic Problems
In the "Ptice" problem, we had three different ways to make the short patterns (like "ABC") match the length of the exam questions:

Fixed Multiplier (Manual Padding):

Method: Multiply the string by a fixed number, like pattern * 34.

Cons: Not flexible. It only works if we know the maximum number of questions (e.g., 100).

The Modulo Operator (%):

Method: Use pattern[i % len(pattern)] inside the loop.

Pros: The most professional and memory-efficient way. It works for any length without creating new long strings.

The while Loop (Dynamic Padding):

Method: Use while len(pattern) < questions: pattern += pattern.

Pros: Very flexible and scales automatically to any input size.

Conclusion: For Backend Development, the Modulo (%) approach is the best "Clean Code" practice because it saves memory and handles any data size perfectly.
"""

"""
questions=int(input())
key=input()
A='ABC'
B='BABC'
C='CCAABB'
a_score=0
b_score=0
c_score=0

while len(A)<questions: A+=A or A+="ABC"
while len(B)<questions: B+=B
while len(C)<questions: C+=C

for i in range(questions):
    if A[i]==key[i]: a_score+=1
    if B[i]==key[i]: b_score+=1
    if C[i]==key[i]: c_score+=1

m=max(a_score,b_score,c_score)
print(m)

if a_score==m:
    print('Adrian')
if b_score==m:
    print('Bruno')
if c_score==m:
    print('Goran')
"""


# # 3. DMOJ problem ccc02j2, AmeriCanadian
# canadian_accent = ""

# while True:
#     american_accent = input()
#     if american_accent == "quit!":
#         break
#     if len(american_accent) > 4:
#         if american_accent[-3] not in "aeiouy" and american_accent[-2:] == "or":
#             canadian_accent = american_accent[:-2] + "our"
#             print(canadian_accent)
#         else:
#             print(american_accent)
#     else:
#         print(american_accent)


# # 4. DMOJ problem ecoo13r1p1, Take a Number
# n = int(input())
# action = ""

# count_t = 0
# count_w = 0

# while action != "EOF":
#     action = input()
#     if action == "TAKE":
#         count_t += 1
#         count_w += 1
#         if n in range(1, 999):
#             n += 1
#         elif n == 999:
#             n = 1
#     elif action == "SERVE":
#         count_w -= 1
#     elif action == "CLOSE":
#         print(count_t, count_w, n)
#         count_t = 0
#         count_w = 0


""""
n = int(input())
action = ""

count_t = 0
count_w = 0

while action != "EOF":
    action = input()
    if action == "TAKE":
        count_t += 1
        count_w += 1
        n += 1
        if n == 1000:
            n = 1
    elif action == "SERVE":
        count_w -= 1
    elif action == "CLOSE":    
        print(count_t, count_w, n)
        count_t = 0
        count_w = 0
"""

# # 5. DMOJ problem ecoo15r1p1, When You Eat Your Smarties
# red = 0
# orange = 0
# blue = 0
# green = 0
# yellow = 0
# pink = 0
# violet = 0
# brown = 0

# box_count = 0

# while box_count < 10:
#     word = input()

#     if word == "red":
#         red += 1
#     elif word == "orange":
#         orange += 1
#     elif word == "blue":
#         blue += 1
#     elif word == "green":
#         green += 1
#     elif word == "yellow":
#         yellow += 1
#     elif word == "pink":
#         pink += 1
#     elif word == "violet":
#         violet += 1
#     elif word == "brown":
#         brown += 1

#     elif word == "end of box":
#         box_count += 1

#         red_time = red * 16
#         orange_time = ((orange + 6) // 7) * 13
#         blue_time = ((blue + 6) // 7) * 13
#         green_time = ((green + 6) // 7) * 13
#         yellow_time = ((yellow + 6) // 7) * 13
#         pink_time = ((pink + 6) // 7) * 13
#         violet_time = ((violet + 6) // 7) * 13
#         brown_time = ((brown + 6) // 7) * 13

#         total_time = (
#             red_time
#             + orange_time
#             + blue_time
#             + green_time
#             + yellow_time
#             + pink_time
#             + violet_time
#             + brown_time
#         )

#         print(total_time)

#         red = 0
#         orange = 0
#         blue = 0
#         green = 0
#         yellow = 0
#         pink = 0
#         violet = 0
#         brown = 0

"""
# 5. DMOJ problem ecoo15r1p1 - Professional Version
box_count = 0

while box_count < 10:
    counts = {
        "orange": 0, "blue": 0, "green": 0, "yellow": 0,
        "pink": 0, "violet": 0, "brown": 0, "red": 0
    }
    
    while True:
        word = input().strip()
        
        if word == "end of box":
            total_time = 0
            for color, count in counts.items():
                if color == "red":
                    total_time += count * 16
                else:
                    total_time += ((count + 6) // 7) * 13
            
            print(total_time)
            box_count += 1
            break
        
        # إذا كان اللون موجود في القاموس، زود عداده
        if word in counts:
            counts[word] += 1
"""


# # 6. DMOJ problem ccc19j3, Cold Compress
# n = int(input())

# for i in range(n):
#     line = input()
#     compressed_parts = []
#     count_j = 1
#     for j in range(
#         len(line) - 1
#     ):  # إستخدمنا -1 علشان ما يقارنش إخر حرف بإل بعده فالبرنامج يضرب
#         if line[j] == line[j + 1]:
#             count_j += 1
#         else:
#             compressed_parts.append(f"{count_j} {line[j]}")
#             count_j = 1

#     compressed_parts.append(
#         f"{count_j} {line[-1]}"
#     )  # طبعنا بره ضروري علشان أخر بلوك مش هيدخل ال إيلس ويطبع فيطبع لما نخرج من اخر دورة و يتحفظ
#     print(" ".join(compressed_parts))

""" wow 
# المتغير الأول: عدد السطور الكلي المطلوب معالجتها
num_lines = int(input())

encoded_lines = []

for _ in range(num_lines):
    line = input()
    pairs = []
    
    # الـ Index اللي بنتحرك بيه يدوي داخل السطر
    i = 0
    
    # اللوب الكبيرة: بتمر على السطر بالكامل
    while i < len(line):
        # المتغير الثاني: عداد تكرار الحرف الواحد (بيبدأ من صفر لكل كتلة جديدة)
        char_count = 0
        current_char = line[i]
        
        # اللوب الصغيرة: "تلتهم" كل الحروف المتشابهة المتتالية
        # i < len(line) هي شرط الأمان عشان م نطلعش بره حدود السطر
        while i < len(line) and line[i] == current_char:
            char_count += 1
            i += 1
            
        # إضافة النتيجة (العدد ثم الحرف) إلى قائمة السطر الحالي
        pairs.append(f"{char_count} {current_char}")

    # تجميع أجزاء السطر المشفر بمسافات وإضافته للقائمة الكبيرة
    encoded_lines.append(" ".join(pairs))

# طباعة كل السطور المشفرة، كل سطر في خط جديد
print("\n".join(encoded_lines))
"""
