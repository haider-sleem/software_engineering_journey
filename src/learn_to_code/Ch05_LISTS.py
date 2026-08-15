# Chapter Exercises page 182

# # 1. DMOJ problem ccc07j3, Deal or No Deal Calculator
# briefcases = {
#     1: 100,
#     2: 500,
#     3: 1000,
#     4: 5000,
#     5: 10000,
#     6: 25000,
#     7: 50000,
#     8: 100000,
#     9: 500000,
#     10: 1000000,
# }

# opened_cases = int(input())
# for i in range(opened_cases):
#     n = int(input())
#     del briefcases[n]
# total = sum(briefcases.values())
# aver = total / len(briefcases)

# offer = int(input())

# if offer > aver:
#     print("deal")
# else:
#     print("no deal")


# # 2. DMOJ problem coci17c1p1, Cezar
# #  بناء الكوتشينة كاملة (52 ورقة) داخل قائمة
# deck = (
#     [2, 3, 4, 5, 6, 7, 8, 9, 11] * 4
#     + [10] * 16
# )

# n = int(input())

# current_sum = 0
# for i in range(n):
#     card = int(input())
#     current_sum += card
#     deck.remove(card)
# X = 21 - current_sum

# greater_than_X = 0
# less_than_or_equal_to_X = 0

# for card_value in deck:
#     if card_value > X:
#         greater_than_X += 1
#     else:
#         less_than_or_equal_to_X += 1

# if greater_than_X >= less_than_or_equal_to_X:
#     print("DOSTA")
# else:
#     print("VUCI")


# # 3. DMOJ problem coci18c2p1, Preokret
# first_half = 48 // 2 * 60
# totalA = int(input())
# totalAB = 0
# lstA = []
# for i in range(totalA):
#     timeA = int(input())
#     lstA.append(timeA)
#     if timeA <= first_half:
#         totalAB += 1

# totalB = int(input())
# lstB = []
# for i in range(totalB):
#     timeB = int(input())
#     lstB.append(timeB)
#     if timeB <= first_half:
#         totalAB += 1

# print(totalAB)


# lstAB = lstA + lstB
# lstAB.sort()

# scoreA = 0
# scoreB = 0
# turnarounds = 0
# leader = "No one"
# for time in lstAB:
#     if time in lstA:
#         scoreA += 1
#     if time in lstB:
#         scoreB += 1

#     if scoreA > scoreB:
#         if leader == "B":
#             turnarounds += 1
#         leader = "A"

#     elif scoreB > scoreA:
#         if leader == "A":
#             turnarounds += 1
#         leader = "B"

# print(turnarounds)


"""
events = []

totalA = int(input())
for i in range(totalA):
    timeA = int(input())
    events.append((timeA, "A"))

totalB = int(input())
for i in range(totalB):
    timeB = int(input())
    events.append((timeB, "B"))

events.sort()

first_half = 48 // 2 * 60
total_first_half_points = 0

scoreA = 0
scoreB = 0

turnarounds = 0
leader = None      # آخر متقدم فعلي

for time, team in events:

    if time <= first_half:
        total_first_half_points += 1

    if team == "A":
        scoreA += 1
    else:
        scoreB += 1


    if scoreA > scoreB:

        if leader == "B":
            turnarounds += 1

        leader = "A"


    elif scoreB > scoreA:

        if leader == "A":
            turnarounds += 1

        leader = "B"


print(total_first_half_points)
print(turnarounds)

"""

## 4. DMOJ problem ccc00s2, Babbling Brooks (Check out Python’s round function.)
# n = int(input())
# lst_quantity = []
# for i in range(n):
#     lst_quantity.append(float(input()))

# while True:
#     event = int(input())

#     if event == 77:
#         break

#     elif event == 99:
#         stream_num = int(input())
#         percentage = int(input())

#         idx = stream_num - 1
#         original_flow = lst_quantity.pop(idx)

#         left_fork = (original_flow * percentage) / 100
#         right_fork = original_flow - left_fork

#         lst_quantity.insert(idx, right_fork)
#         lst_quantity.insert(idx, left_fork)

#     elif event == 88:
#         stream_num = int(input())

#         idx = stream_num - 1
#         lst_quantity[idx] += lst_quantity.pop(idx + 1)

# output_rivers = [str(int(round(flow))) for flow in lst_quantity] ## round() approximates values, int() converts to whole numbers, and str() allows string joining for output.

# print(" ".join(output_rivers))


# # 5. DMOJ problem ecoo18r1p1, Willow’s Wild Ride
# for dataset in range(10):
#     t_n = input().split()
#     time = int(t_n[0])
#     days = int(t_n[1])

#     days_for_play = 0
#     for day in range(days):
#         status = input()
#         if status == "B":
#             days_for_play += time

#         if days_for_play > 0:
#             days_for_play -= 1
#     print(days_for_play)


# # 6. DMOJ problem ecoo19r1p1, Free Shirts
# for dataset in range(10):
#     line1 = input().split()
#     n = int(line1[0])
#     m = int(line1[1])
#     d = int(line1[2])

#     if m > 0:
#         days = list(map(int, input().split()))
#     else:
#         days = []

#     clean_shirts = n
#     total_shirts = n
#     washing = 0
#     for day in range(1,d+1):
#         if clean_shirts == 0:
#             washing += 1
#             clean_shirts = total_shirts
#         if day in days:
#             total_shirts += days.count(day)
#             clean_shirts += days.count(day)


#         clean_shirts -= 1

#     print(washing)


# # 7. DMOJ problem dmopc14c7p2, Tides
# n = int(input())
# levels = list(map(int, input().split()))

# high = max(levels)
# low = min(levels)

# high_index = levels.index(high)
# low_index = levels.index(low)

# status = True

# if low_index > high_index:
#     status = False
# else:
#     for i in range(low_index, high_index):
#         if levels[i] >= levels[i + 1]:
#             status = False

# if status:
#     print(high - low)
# else:
#     print("unknown")

"""
# حل واحد عبقري من على الموقع 

number = int(input())
heights = input()
heights = heights.split()
heights = [int(height) for height in heights]

minIndex = heights.index(min(heights))
maxIndex = heights.index(max(heights))
heights = heights[minIndex:maxIndex + 1]

if len(heights) > 0 and sorted(heights) == heights:
    print(heights[-1] - heights[0])
else:
    print("unknown")
"""


# # 8. DMOJ problem wac3p3, Wesley Plays DDR
# s = input()
# n = int(input())
# combos = []
# for _ in range(n):
#     ci, pi = input().split()
#     pi = int(pi)
#     combos.append((ci, pi))

# point = len(s)

# i = 0

# while i < len(s):
#     longest_combo_len = 0
#     combo_points = 0

#     for ci, pi in combos:
#         if s[i : i + len(ci)] == ci:
#             if len(ci) > longest_combo_len:
#                 longest_combo_len = len(ci)
#                 combo_points = pi

#     if longest_combo_len > 0:
#         point += combo_points
#         i += longest_combo_len
#     else:
#         i += 1

# print(point)
"""
# حل واحد عبقري من على الموقع 

s = input()
m = int(input())
ans = len(s)
assert len(s) >= 1 and len(s) <= 1000
assert m >= 1 and m <= 5
d = []
for i in range(len(s)):
    c = s[i]
    assert c in "UDLR"
for i in range(m):
    c = input().split()
    d.append((c[0],int(c[1])))
    assert len(c[0]) >= 2 and len(c[0]) <= 5
    assert int(c[1]) >= 2 and int(c[1]) <= 1000
    
dd = sorted(d, key=lambda x: len(x[0]), reverse=True)
idx = 0
while idx < len(s):
    f = 1
    for a,b in dd:
        if s[idx:idx+len(a)] == a:
            f = 0
            ans += b
            idx += len(a)
            break
    if f == 1: idx += 1
print(ans)
"""

# 9. DMOJ problem ecoo18r1p2, Rue’s Rings (If you use f-strings here,you’ll need a way to include the { and } symbols themselves. You can include a { in the f-string by using {{ and a } by using }}.)
# for i in range(10):

#     n = int(input())

#     lowest = float('inf')
#     s = []

#     for i in range(n):
#         line = input().split()

#         id = int(line[0])
#         rounds_n = int(line[1])

#         diameters = list(map(int, line[2:]))

#         low = min(diameters)

#         if low < lowest:
#             lowest = low
#             s = [id]
#         elif low == lowest:
#             s.append(id)

#     S_string = ",".join(str(x) for x in sorted(s))

#     print(f"{lowest} {{{S_string}}}")


# # 10. DMOJ problem coci19c5p1, Emacs

"""
# 1. فكرة الحل: عَدّ المستطيلات عن طريق لقط "الزاوية فوق شمال" لكل مستطيل فقط.
# 2. الكفاءة: حل خارق وسريع جداً (Memory = O(1)) لأنه يقرأ المصفوفة بدون استهلاك للذاكرة.
"""
# n, m = map(int, input().split())

# picture = []
# for _ in range(n):
#     picture.append(input())

# rectangles_count = 0

# for row in range(n):
#     for col in range(m):
#         if picture[row][col] == "*":
#             is_top_left = True

#             if row > 0 and picture[row - 1][col] == "*":
#                 is_top_left = False

#             if col > 0 and picture[row][col - 1] == "*":
#                 is_top_left = False

#             if is_top_left:
#                 rectangles_count += 1

# print(rectangles_count)


"""
# 1. فكرة الحل: استخدام خوارزمية الفيضان (Flood Fill) لتمسح وتعد أي كتلة متصلة مهما كان شكلها.
# 2. الكفاءة: حل جوكر ومرن للغاية ينفع لكل الأشكال المعقدة، لكنه يستهلك مساحة في الذاكرة (RAM).
"""
# height_width = input().strip().split()

# n = int(height_width[0])
# m = int(height_width[1])

# grid = []

# for _ in range(n):
#     text_input = input().strip()
#     grid.append(list(text_input))

# count = 0
# for r in range(n):
#     for c in range(m):
#         if grid[r][c] == "*":
#             count += 1

#             to_visit = [(r, c)]
#             while to_visit:
#                 cr, cc = to_visit.pop()

#                 if cr < 0 or cr >= n or cc < 0 or cc >= m:
#                     continue

#                 if grid[cr][cc] != "*":
#                     continue

#                 grid[cr][cc] = "."

#                 to_visit.append((cr + 1, cc))
#                 to_visit.append((cr - 1, cc))
#                 to_visit.append((cr, cc + 1))
#                 to_visit.append((cr, cc - 1))

# print(count)


# 11. DMOJ problem coci20c2p1, Crtanje (You’ll need to support rows from –100 to 100. But how do we support negative-indexed rows when Python lists start at index 0? Here’s a trick: use index x + 100 any time you need access to row x. That shifts the row numbers to be between 0 and 200 rather than between –100 and 100. Also, one small annoyance here with strings: \ is a special character, so you’ll have to use '\\' rather than '\' if you want a \ character.)

############### الحل الخطأ
# n = int(input())
# changes = input().strip()

# path = [0]
# count = 0
# for i in changes:
#     if i == "+":
#         count += 1
#     elif i == "-":
#         count -= 1
#     elif i == "=":
#         pass
#     path.append(count)

# max_val = max(path)
# min_val = min(path)

# rows = max_val - min_val + 1
# cols = n

# grid = []
# for _ in range(rows):
#     grid.append(["."] * cols)

# for i in range(n):
#     current = path[i]
#     next_val = path[i + 1]

#     row = max_val - current
#     col = i

#     if next_val > current:
#         grid[row][col] = "/"
#     elif next_val < current:
#         grid[row + 1][col] = "\\"
#     else:
#         grid[row][col] = "_"

# for row in grid:
#     print(" ".join(row))


# ######################### الحل بعد التصحيح فكرة الحل تكبير الجريد و طباعة الرسمة فقط في الاخر

# n = int(input())
# changes = input().strip()

# # 1. بناء المسار التقليدي
# path = [0]
# count = 0
# for i in changes:
#     if i == "+":
#         count += 1
#     elif i == "-":
#         count -= 1
#     elif i == "=":
#         pass
#     path.append(count)

# # 2. تكبير قماش الرسم لـ 4 أضعاف لضمان الأمان الكامل من فوق ومن تحت
# rows = 4 * n
# cols = n

# grid = []
# for _ in range(rows):
#     grid.append(["."] * cols)

# # 3. إسقاط الرموز مع جعل نقطة المنتصف (2 * n) هي الصفر الثابت
# for i in range(n):
#     current = path[i]
#     next_val = path[i + 1]

#     # نقطة المنتصف 2*n تحمينا تماماً من الصعود والنزول الحاد
#     row = (2 * n) - current
#     col = i

#     if next_val > current:
#         grid[row][col] = "/"
#     elif next_val < current:
#         grid[row + 1][col] = "\\"
#     else:
#         grid[row][col] = "_"

# # 4. طباعة وقص الأسطر الفاضية بالملي
# empty_row = "." * n

# for row in grid:
#     row_str = "".join(row)
#     if row_str != empty_row:
#         print(row_str)


######################## الحل بالقاموس وعدم رسم الماتريكس كاملا ال بعد تحديد اماكن الرسم
# n = int(input())
# changes = input().strip()

# path = [0]
# count = 0
# for i in changes:
#     if i == "+":
#         count += 1
#     elif i == "-":
#         count -= 1
#     elif i == "=":
#         pass
#     path.append(count)

# drawn_cells = {}

# for i in range(n):
#     current = path[i]
#     next_val = path[i + 1]
#     col = i

#     if next_val > current:
#         row = current
#         symbol = "/"
#     elif next_val < current:
#         row = next_val
#         symbol = "\\"
#     else:
#         row = current
#         symbol = "_"

#     drawn_cells[(row, col)] = symbol

# all_rows = [key[0] for key in drawn_cells.keys()]
# max_r = max(all_rows)
# min_r = min(all_rows)

# for r in range(max_r, min_r - 1, -1):
#     row_output = []
#     for c in range(n):
#         if (r, c) in drawn_cells:
#             row_output.append(drawn_cells[(r, c)])
#         else:
#             row_output.append(".")
#     print("".join(row_output))


# 12. DMOJ problem dmopc19c5p2, Charlie’s Crazy Conquest (You’ll have to be careful with indices and the game rules for this one!)

# # أول محاولة حل خاطئة
# n_h = input().strip().split()

# n, h = map(int, n_h)

# charly_moves = []
# for _ in range(n):
#     charly = input("enter move").split()
#     charly_moves.append((charly[0], int(charly[1])))
# # [('A', 50), ('D', 10), ('A', 100)]
# bot_moves = []
# for _ in range(n):
#     bot = input(()).split()
#     bot_moves.append((bot[0], int(bot[1])))
# # [('A', 90), ('D', 0), ('A', 0)]

# charly_energy, bot_energy = h, h

# for indix in range(n):
#     i = charly_moves[indix]
#     j = bot_moves[indix]

#     # 1. تنفيذ الهجمات الحالية للطرفين معاً
#     if i[0] == "A":
#         charlie_attack_dodged = indix > 0 and bot_moves[indix - 1][0] == "D"
#         if not charlie_attack_dodged:
#             bot_energy -= i[1]

#     if j[0] == "A":
#         bot_attack_dodged = indix > 0 and charly_moves[indix - 1][0] == "D"
#         if not bot_attack_dodged:
#             charly_energy -= j[1]

#     # 2. تطبيق شرط الـ (Terminate) فوراً بعد الهجوم وقبل حساب عقوبات الـ Dodge
#     if charly_energy <= 0 or bot_energy <= 0:
#         break

#     # 3. حساب عقوبات التفادي الفاشل (لا نصل هنا إلا لو كان الاثنان أحياء بعد الهجوم)
#     if i[0] == "D" and (indix + 1 == n or bot_moves[indix + 1][0] != "A"):
#         charly_energy -= i[1]

#     if j[0] == "D" and (indix + 1 == n or charly_moves[indix + 1][0] != "A"):
#         bot_energy -= j[1]

#     # 4. تحقق أخير بعد العقوبات وقبل الانتقال للدور القادم
#     if charly_energy <= 0 or bot_energy <= 0:
#         break

# # حساب النتيجة النهائية بالخارج بكل أمان
# if charly_energy <= 0 and bot_energy <= 0:
#     print("TIE")
# elif charly_energy <= 0:
#     print("DEFEAT")
# elif bot_energy <= 0:
#     print("VICTORY")
# else:
#     print("TIE")


# # الحل الصحيح بعد 26 حل خطأ بمساعدة أدوات الذكاء المجانية
# # 1. قراءة البيانات بنفس طريقتك البسيطة
# n_h = input().strip().split()
# n, h = map(int, n_h)

# charly_moves = []
# for _ in range(n):
#     charly = input().strip().split()
#     charly_moves.append((charly[0], int(charly[1])))

# bot_moves = []
# for _ in range(n):
#     bot = input().strip().split()
#     bot_moves.append((bot[0], int(bot[1])))

# charly_energy, bot_energy = h, h

# # المتغير المنطقي لمتابعة تأثير تفادي البوت على الدور التالي
# bot_had_dodge = False

# # 2. اللوب الصريحة بنفس أسلوبك
# for indix in range(n):
#     i = charly_moves[indix]
#     j = bot_moves[indix]

#     # --- الحالة الأولى: لو البوت كان مجهز Dodge من الدور السابق ---
#     if bot_had_dodge:
#         if i[0] == "A":
#             bot_had_dodge = False
#             if j[0] == "D":
#                 bot_had_dodge = True
#             else:
#                 charly_energy -= j[1]

#             if charly_energy <= 0 or bot_energy <= 0:
#                 break
#             continue

#         elif i[0] == "D":
#             bot_had_dodge = False
#             # عقاب البوت على حركته القديمة
#             bot_energy -= bot_moves[indix - 1][1]

#             if bot_energy <= 0:
#                 break

#             if j[0] == "D":
#                 bot_had_dodge = True
#                 charly_energy -= i[1]

#             if charly_energy <= 0 or bot_energy <= 0:
#                 break
#             continue

#     # --- الحالة الثانية: لو مفيش تأثير من الدور السابق (مواجهة مباشرة) ---
#     if i[0] == "A" and j[0] == "D":
#         bot_had_dodge = True
#         bot_energy -= i[1]  # عقاب البوت الفوري (self-humility)

#     elif i[0] == "D" and j[0] == "A":
#         pass  # تشارلي يتفادى هجوم البوت بنجاح

#     elif i[0] == "A" and j[0] == "A":
#         bot_energy -= i[1]
#         if bot_energy <= 0:
#             break
#         charly_energy -= j[1]
#         if charly_energy <= 0:
#             break

#     else:  # حالة D ضد D
#         bot_had_dodge = True
#         charly_energy -= i[1]  # عقاب تشارلي الفوري

#     # التحقق المعتاد في نهاية الدور
#     if charly_energy <= 0 or bot_energy <= 0:
#         break

# # 3. عقاب الدور الأخير خارج اللوب لو البوت ختم بـ Dodge ولم يمت أحد
# if charly_energy > 0 and bot_energy > 0:
#     if bot_moves[-1][0] == 'D':
#         bot_energy -= bot_moves[-1][1]

# # 4. حساب النتيجة النهائية بالخارج بكل أمان بأسمائك الصحيحة
# if charly_energy <= 0 and bot_energy <= 0:
#     print("TIE")
# elif charly_energy <= 0:
#     print("DEFEAT")
# elif bot_energy <= 0:
#     print("VICTORY")
# else:
#     print("TIE")
