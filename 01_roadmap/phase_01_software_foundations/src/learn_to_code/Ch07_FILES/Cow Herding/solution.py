# 7. USACO 2019 February Bronze Contest problem Sleepy Cow Herding
# Source : https://usaco.org/index.php?page=viewproblem2&cpid=915

import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(current_path, "herding.in")
out_path = os.path.join(current_path, "herding.out")

with open(in_path, "r") as file_input:
    cows = list(map(int, file_input.readline().split()))

cows.sort()
a, b, c = cows

# الفجوة = عدد الخانات الفاضية بين بقرتين متتاليتين
gap1 = b - a - 1
gap2 = c - b - 1

# ---------- الحد الأدنى ----------
if gap1 == 0 and gap2 == 0:
    min_moves = 0
elif gap1 == 1 or gap2 == 1:
    min_moves = 1
else:
    min_moves = 2

# ---------- الحد الأقصى ----------
max_moves = max(gap1, gap2)

with open(out_path, "w") as file_output:
    file_output.write(str(min_moves) + "\n")
    file_output.write(str(max_moves) + "\n")