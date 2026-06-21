# 4. USACO 2019 December Bronze Contest problem Cow Gymnastics


import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(current_path, "Gymnastics.in")
out_path = os.path.join(current_path, "Gymnastics.out")

with open(in_path, "r") as file_input:
    k, n = map(int, file_input.readline().split())

    sessions = []
    for _ in range(k):
        sessions.append(list(map(int, file_input.readline().split())))

count = 0
for cowA in range(1, n + 1):
    for cowB in range(cowA + 1, n + 1):
        cowA_is_better = all(
            session.index(cowA) < session.index(cowB) for session in sessions
        )
        cowB_is_better = all(
            session.index(cowB) < session.index(cowA) for session in sessions
        )
        if cowA_is_better or cowB_is_better:
            count += 1

with open(out_path, "w") as file_output:
    file_output.write(str(count) + "\n")
