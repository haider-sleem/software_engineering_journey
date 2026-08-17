# Chapter Exercises page 220

# 1. DMOJ problem ccc13s1, From 1987 to 2013
# y = int(input())

# def next_unique_num(y):
#     i = y + 1
#     while True:
#         s = str(i)
#         x = set(s)
#         if len(x) == len(s):
#             return int(s)
#         i = i + 1

# print(next_unique_num(y))


# # 2. DMOJ problem ccc18j3, Are we there yet?
# dists = list(map(int, input().split()))

# for i in range(1, 6):
#     row = []
#     for j in range(1, 6):
#         if i == j:
#             row.append(0)
#         else:
#             start = min(i, j)
#             end = max(i, j)
#             distance = sum(dists[start-1 : end-1])
#             row.append(distance)

#     print(*(row))

## 3. DMOJ problem  ecoo12r1p2, Decoding DNA
# def reverse_complement(sequence):
#     complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

#     result = ""

#     for ch in reversed(sequence):
#         result += complement[ch]

#     return result


# def dna_to_rna(sequence):
#     mapping = {"A": "U", "T": "A", "C": "G", "G": "C"}

#     result = ""

#     for ch in sequence:
#         result += mapping[ch]

#     return result


# for case in range(1, 6):
#     dna = input().strip()

#     promoter_index = dna.find("TATAAT")

#     start = promoter_index + 10

#     end = len(dna)

#     for i in range(start, len(dna) - 5):
#         left = dna[i : i + 6]

#         target = reverse_complement(left)

#         if dna.find(target, i + 6) != -1:
#             end = i
#             break

#     transcription_unit = dna[start:end]

#     rna = dna_to_rna(transcription_unit)

#     print(f"{case}: {rna}")


# # 4. DMOJ problem crci07p1, Platforme
# n = int(input())
# platforms = []
# for _ in range(n):
#     y, x1, x2 = map(int, input().split())
#     platforms.append((y, x1, x2))

# platforms.sort()

# ground = [0] * 10001
# total_length = 0

# for y, x1, x2 in platforms:
#     total_length += y - ground[x1]

#     total_length += y - ground[x2 - 1]

#     for i in range(x1, x2):
#         ground[i] = y

# print(total_length)


# # 5. DMOJ problem coci13c2p2, Misa
# r, c = map(int, input().split())

# grid = []

# for _ in range(r):
#     grid.append(list(input().strip()))

# directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# current_handshakes = 0

# # حساب المصافحات الحالية
# for row in range(r):
#     for col in range(c):
#         if grid[row][col] == "o":
#             for dr, dc in directions:
#                 nr = row + dr
#                 nc = col + dc

#                 if 0 <= nr < r and 0 <= nc < c:
#                     if grid[nr][nc] == "o":
#                         current_handshakes += 1

# # كل مصافحة اتعدت مرتين
# current_handshakes //= 2

# best_extra = 0
# empty_exists = False

# # تجربة كل مكان فارغ
# for row in range(r):
#     for col in range(c):
#         if grid[row][col] == ".":
#             empty_exists = True

#             count = 0

#             for dr, dc in directions:
#                 nr = row + dr
#                 nc = col + dc

#                 if 0 <= nr < r and 0 <= nc < c:
#                     if grid[nr][nc] == "o":
#                         count += 1

#             best_extra = max(best_extra, count)

# print(current_handshakes + best_extra)

# ############################################
# # قراءة أبعاد المصفوفة
# R, C = map(int, input().split())
# grid = [list(input()) for _ in range(R)]


# # دالة مساعدة لحساب عدد الأشخاص حول نقطة معينة
# def count_neighbors(r, c):
#     count = 0
#     # التحقق من الجيران الثمانية
#     for dr in [-1, 0, 1]:
#         for dc in [-1, 0, 1]:
#             if dr == 0 and dc == 0:
#                 continue
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "o":
#                 count += 1
#     return count


# # 1. حساب المصافحات الموجودة حالياً
# total_handshakes = 0
# for r in range(R):
#     for c in range(C):
#         if grid[r][c] == "o":
#             total_handshakes += count_neighbors(r, c)
# # نقسم على 2 لأن كل مصافحة حُسبت من الطرفين
# total_handshakes //= 2

# # 2. البحث عن أفضل مكان لميركو
# max_new_handshakes = 0
# for r in range(R):
#     for c in range(C):
#         if grid[r][c] == ".":
#             # كم شخص سيصافح ميركو إذا جلس هنا؟
#             max_new_handshakes = max(max_new_handshakes, count_neighbors(r, c))

# # النتيجة النهائية: المصافحات القديمة + إضافة ميركو
# print(total_handshakes + max_new_handshakes)


# 6. Revisit some of the exercises from Chapter 5 and improve your solutions by using functions. I particularly suggest revisiting DMOJ problem coci18c2p1 (Preokret) and DMOJ problem ccc00s2 (Babbling Brooks).

# # A : DMOJ problem coci18c2p1 (Preokret)
# def calculate_points(times):
#     points = 0
#     for t in times:
#         if t <= 1440:
#             points += 1
#     return points


# A = int(input())
# A_times = [int(input()) for _ in range(A)]

# B = int(input())
# B_times = [int(input()) for _ in range(B)]

# a_pts = calculate_points(A_times)
# b_pts = calculate_points(B_times)
# print(a_pts + b_pts)

# all = []
# for t in A_times:
#     all.append((t, "A"))
# for t in B_times:
#     all.append((t, "B"))

# score_a = 0
# score_b = 0
# turnarounds = 0
# leader = 0

# for time, team in sorted(all):
#     if team == "A":
#         score_a += 1
#     else:
#         score_b += 1

#     if score_a > score_b and leader == 0:
#         leader = 1
#     elif score_b > score_a and leader == 0:
#         leader = 2
#     elif score_a > score_b and leader == 2:
#         turnarounds += 1
#         leader = 1
#     elif score_b > score_a and leader == 1:
#         turnarounds += 1
#         leader = 2


# print(turnarounds)


# # B : DMOJ problem ccc00s2 (Babbling Brooks).
# n = int(input())
# n_flow = [int(input()) for _ in range(n)]


# def split_river(n_flow, river_num, percentage):
#     current_flow = n_flow[river_num - 1]
#     left_flow = current_flow * percentage / 100
#     right_flow = current_flow - left_flow

#     n_flow[river_num - 1] = left_flow
#     n_flow.insert(river_num, right_flow)


# def join_rivers(n_flow, river_num):
#     current_flow = n_flow[river_num - 1]
#     next_flow = n_flow[river_num]

#     n_flow[river_num - 1] = current_flow + next_flow
#     del n_flow[river_num]


# while True:
#     action = int(input())
#     if action == 77:
#         break
#     elif action == 99:
#         split_river(n_flow, int(input()), int(input()))
#     elif action == 88:
#         join_rivers(n_flow, int(input()))

# print(" ".join(str(int(round(flow))) for flow in n_flow))
