# 2. USACO 2017 February Bronze Contest problem Why Did the Cow Cross the Road
import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(current_path, "crossroad.in")
out_path = os.path.join(current_path, "crossroad.out")

with open(in_path, "r") as file_input, open(out_path, "w") as file_output:
    number_of_views = int(file_input.readline())
    count = 0
    all_cows = []

    for _ in range(number_of_views):
        cow = file_input.readline().split()

        found = False

        for i in range(len(all_cows)):
            if all_cows[i][0] == cow[0]:
                found = True

                if all_cows[i][1] != cow[1]:
                    count += 1

                all_cows[i][1] = cow[1]

                break

        if not found:
            all_cows.append(cow)
    file_output.write(str(count) + "\n")
