# 3. USACO 2017 US Open Bronze Contest problem The Lost Cow
# Source: https://usaco.org/index.php?page=viewproblem2&cpid=735

import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(current_path, "lostcow.in")
out_path = os.path.join(current_path, "lostcow.out")


with open(in_path, "r") as file_input:
    x, y = map(int, file_input.readline().split())


position = x
move = 1
distance = 0

while True:
    target = x + move
    if min(position, target) <= y <= max(position, target):
        distance += abs(position - y)
        break
    distance += abs(target - position)
    move *= -2
    position = target

with open(out_path, "w") as file_output:
    file_output.write(str(distance) + "\n")
