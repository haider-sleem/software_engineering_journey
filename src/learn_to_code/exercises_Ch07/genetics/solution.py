# 5. USACO 2017 US Open Bronze Contest problem Bovine Genomics
# Source : https://usaco.org/index.php?page=viewproblem2&cpid=736

import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(current_path, "cownomics.in")
out_path = os.path.join(current_path, "cownomics.out")

with open(in_path, "r") as file_input:
    n, m = map(int, file_input.readline().split())

    spotty = []
    plain = []

    for _ in range(n):
        spotty.append(file_input.readline().strip())

    for _ in range(n):
        plain.append(file_input.readline().strip())

count = 0

for position in range(m):
    spotty_letters = set()
    plain_letters = set()

    for cow in spotty:
        spotty_letters.add(cow[position])

    for cow in plain:
        plain_letters.add(cow[position])

    if spotty_letters.isdisjoint(plain_letters):
        count += 1

with open(out_path, "w") as file_output:
    file_output.write(str(count) + "\n")
