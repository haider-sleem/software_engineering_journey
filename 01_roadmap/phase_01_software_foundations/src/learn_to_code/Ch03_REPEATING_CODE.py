# Problem #5: Three Cups This is DMOJ problem coci06c5p1 page 82


# Chapter Exercises page 105

# # 1. DMOJ problem wc17c3j3, Uncrackable
# password = input()

# lower_count = 0
# upper_count = 0
# digit_count = 0

# for char in password:
#     if char.islower():
#         lower_count += 1
#     elif char.isupper():
#         upper_count += 1
#     elif char.isdigit():
#         digit_count += 1

# if (
#     8 <= len(password) <= 12
#     and lower_count >= 3
#     and upper_count >= 2
#     and digit_count >= 1
# ):
#     print("Valid")
# else:
#     print("Invalid")
# """
# Best performance:
# if num_upper < 2 or num_lower < 3 or num_digit < 1 or len(passw) < 8 or len(passw) > 12:
#     print('Invalid')
# else:
#     print('Valid')
# """


# # 2. DMOJ problem coci18c3p1, Magnus
# honi_count = 0
# wantted_letter = "H"

# word = input()
# for i in word:
#     if i == "H" and wantted_letter == "H":
#         wantted_letter = "O"
#     elif i == "O" and wantted_letter == "O":
#         wantted_letter = "N"
#     elif i == "N" and wantted_letter == "N":
#         wantted_letter = "I"
#     elif i == "I" and wantted_letter == "I":
#         honi_count += 1
#         wantted_letter = "H"

# print(honi_count)


# # 3. DMOJ problem ccc11s1, English or French
# # 1. قراءة عدد الأسطر وتحويله لـ Integer
# n = int(input())

# # 2. تجهيز العدادات خارج اللوب
# t_count = 0
# s_count = 0

# # 3. عمل Loop يلف n من المرات لقراءة كل سطر
# for i in range(n):
#     line = input()
#     # 4. تفصيص كل سطر لحروف وعد المطلوب
#     for char in line:
#         if char == 't' or char == 'T':
#             t_count += 1
#         elif char == 's' or char == 'S':
#             s_count += 1

# if t_count > s_count:
#     print("English")
# else:
#     print("French")

"""
n = int(input())
t_count = 0
s_count = 0

for _ in range(n):
    line = input().lower() # تحويل السطر كله لصغير مرة واحدة لضمان الدقة
    t_count += line.count('t')
    s_count += line.count('s')

if t_count > s_count:
    print("English")
else:
    print("French")
"""

# # 4. DMOJ problem ccc11s2, Multiple Choice
# number_of_q = int(input())

# student_answers = []
# correct_answers = []

# score = 0

# for _ in range(number_of_q):
#     student_answers.append(input())

# for _ in range(number_of_q):
#     correct_answers.append(input())

# for i in range(number_of_q):
#     if student_answers[i] == correct_answers[i]:
#         score += 1

# print(score)

"""
number_of_q = int(input())
student_answers = [input() for i in range(number_of_q)]
correct_answers = [input() for i in range(number_of_q)]
score = 0

for i in range(number_of_q):
    if student_answers[i] == correct_answers[i]:
        score += 1

print(score)


"""


# # 5. DMOJ problem coci12c5p1, Ljestvica
# music_input = input()
# measures = music_input.split("|")
# countA = 0
# countC = 0

# for i in measures:
#     if i[0] in ["A", "D", "E"]:
#         countA += 1
#     elif i[0] in ["C", "F", "G"]:
#         countC += 1
# if countA > countC:
#     print("A-mol")
# elif countC > countA:
#     print("C-dur")
# else:
#     if i[-1] in ["A", "D", "E"]:
#         print("A-mol")
#     elif i[-1] in ["C", "F", "G"]:
#         print("C-dur")


"""

string = input()

c_major = 0
a_minor = 0
for i in range(len(string)):
    if(i == 0 or string[i-1]=="|"):
        if(string[i]=="C" or string[i]=="F" or string[i]=="G"):
            c_major+=1
        if(string[i]=="A" or string[i]=="D" or string[i]=="E"):
            a_minor+=1
            
if(a_minor>c_major):
    print("A-mol")
elif(c_major>a_minor):
    print("C-dur")
else:
    if(string[len(string)-1]=="C"):
        print("C-dur")
    elif(string[len(string)-1]=="A"):
        print("A-mol")
"""


# 6. DMOJ problem coci13c3p1, Rijeci
n = int(input())

a = 1
b = 0

for _ in range(n):
    new_a = b
    new_b = a + b
    a = new_a
    b = new_b

print(a, b)

"""

n = int(input())

a, b = 1, 0  # تعريف المتغيرات في سطر واحد

for _ in range(n):
    # تحديث القيمتين في نفس اللحظة
    a, b = b, a + b

print(a, b)

"""


# # 7. DMOJ problem coci18c4p1, Elder
# current_owner = input()

# owners_history = {current_owner}

# n = int(input())

# for _ in range(n):
#     winner, loser = input().split()

#     if loser == current_owner:
#         current_owner = winner
#         owners_history.add(winner)
# print(current_owner)
# print(len(owners_history))

"""
owner = input()
num_duels = int(input())

count = 1

people = owner
for i in range (num_duels):
    duel = input()

    if duel [0] != owner and duel[2]== owner:
        owner = duel[0]

        if owner not in people:
            count = count + 1 
        people = people + owner

print (owner)
print (count)
"""
