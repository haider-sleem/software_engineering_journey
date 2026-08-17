# Chapter Exercises page 363


# # 1. DMOJ problem dmopc17c1p1, Fujo Neko (The problem talks about using fast input/output. Don’t ignore that!)
# # Source: https://dmoj.ca/problem/dmopc17c1p1
# import sys

# # Use fast input because Q can reach 1,000,000
# input = sys.stdin.readline


# def read_grid(num_rows, num_cols):
#     """Read the grid row by row and return it as a list of strings."""
#     grid = []
#     for _ in range(num_rows):
#         row = input().strip()
#         grid.append(row)
#     return grid


# def find_rows_and_cols_with_beings(grid, num_rows, num_cols):
#     """
#     Scan the entire grid once and record which rows and columns contain a being.

#     Why a Set?
#     A set gives O(1) membership checks (x in set), which is what we need
#     when answering each query. A list would require O(R) or O(C) time per check.

#     Returns two sets: one for row indices, one for column indices.
#     """
#     rows_with_being = set()
#     cols_with_being = set()

#     for row_index in range(num_rows):
#         for col_index in range(num_cols):
#             if grid[row_index][col_index] == 'X':
#                 rows_with_being.add(row_index)
#                 cols_with_being.add(col_index)

#     return rows_with_being, cols_with_being


# def can_saki_see_being(saki_row, saki_col, rows_with_being, cols_with_being):
#     """
#     Return True if any being lies in Saki's row or column.

#     Saki looks north, south, east, and west — which together cover every
#     cell in her row and every cell in her column. So the question reduces to:
#     does her row OR her column contain at least one 'X'?
#     """
#     return saki_row in rows_with_being or saki_col in cols_with_being


# def answer_queries(num_queries, rows_with_being, cols_with_being):
#     """
#     Read each query, determine the answer, and collect all results.

#     Output is batched into a single write call to avoid the overhead
#     of calling print() separately for each of the potentially 1,000,000 queries.

#     Note on input format: the problem gives (col, row), not (row, col).
#     All coordinates are 1-based, so we convert to 0-based by subtracting 1.
#     """
#     results = []

#     for _ in range(num_queries):
#         saki_col, saki_row = map(int, input().split())

#         # Convert from 1-based to 0-based indexing
#         saki_row -= 1
#         saki_col -= 1

#         if can_saki_see_being(saki_row, saki_col, rows_with_being, cols_with_being):
#             results.append('Y')
#         else:
#             results.append('N')

#     sys.stdout.write('\n'.join(results) + '\n')


# def main():
#     num_rows, num_cols = map(int, input().split())
#     grid = read_grid(num_rows, num_cols)

#     rows_with_being, cols_with_being = find_rows_and_cols_with_beings(
#         grid, num_rows, num_cols
#     )

#     num_queries = int(input())
#     answer_queries(num_queries, rows_with_being, cols_with_being)

# main()


# # 2. DMOJ problem coci10c1p2, Profesor
# # Source: https://dmoj.ca/problem/coci10c1p2
# import sys


# def read_input():
#     """Read the input and return the list of desks."""
#     data = sys.stdin.read().split()

#     index = 0
#     num_desks = int(data[index])
#     index += 1

#     desks = []

#     for _ in range(num_desks):
#         left_grade = int(data[index])
#         index += 1

#         right_grade = int(data[index])
#         index += 1

#         desks.append((left_grade, right_grade))

#     return desks


# def find_best_result(desks):
#     """
#     Find the largest consecutive sequence of desks where every desk
#     contains at least one student with the same grade.
#     """

#     last_seen = {}
#     current_run = {}

#     best_count = 0
#     best_grade = float("inf")

#     for desk_index, (left_grade, right_grade) in enumerate(desks):

#         # Process each grade only once if both students have the same grade.
#         for grade in {left_grade, right_grade}:

#             if last_seen.get(grade, -2) == desk_index - 1:
#                 current_run[grade] = current_run.get(grade, 0) + 1
#             else:
#                 current_run[grade] = 1

#             last_seen[grade] = desk_index

#             if (
#                 current_run[grade] > best_count
#                 or (
#                     current_run[grade] == best_count
#                     and grade < best_grade
#                 )
#             ):
#                 best_count = current_run[grade]
#                 best_grade = grade

#     return best_count, best_grade


# def solve():
#     desks = read_input()

#     max_students, best_grade = find_best_result(desks)

#     print(max_students, best_grade)


# if __name__ == "__main__":
#     solve()

"""
import sys

def main():
    input = sys.stdin.buffer.readline
    N = int(input())
    desks = [tuple(map(int, input().split())) for _ in range(N)]

    best_len = 0
    best_grade = 1

    for grade in range(1, 6):
        cur_len = 0
        max_len = 0
        for a, b in desks:
            if a == grade or b == grade:
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = 0
        if max_len > best_len or (max_len == best_len and grade < best_grade):
            best_len = max_len
            best_grade = grade

    print(best_len, best_grade)

if __name__ == "__main__":
    main()
"""


# # 3. DMOJ problem coci19c4p1, Pod starim krovovima (Hint: to maximize the number of empty glasses, you want to put as much liquid as possible in the biggest glasses.)
# # Source: https://dmoj.ca/problem/coci19c4p1
# import sys

# input = sys.stdin.readline


# def solve():
#     n = int(input())

#     glasses = []
#     for i in range(n):
#         amount, volume = map(int, input().split())
#         glasses.append((amount, volume, i))  # keep original index for output ordering

#     total_liquid = sum(amount for amount, volume, _ in glasses)

#     # Sort by volume descending — fill the largest glasses first (Greedy)
#     glasses_by_volume = sorted(glasses, key=lambda g: g[1], reverse=True)

#     # Distribute all liquid into as few glasses as possible
#     result = [0] * n
#     remaining_liquid = total_liquid

#     for amount, volume, original_index in glasses_by_volume:
#         if remaining_liquid <= 0:
#             break
#         fill = min(remaining_liquid, volume)
#         result[original_index] = fill
#         remaining_liquid -= fill

#     empty_count = result.count(0)

#     print(empty_count)
#     print(*result)


# solve()


# # 4. DMOJ problem dmopc20c1p2, Victor’s Moral Dilemma
# # Source: https://dmoj.ca/problem/dmopc20c1p2
# import sys

# input = sys.stdin.readline


# def build_prefix_sum(values):
#     """Return a prefix sum array where prefix[i] is the sum of the first i elements."""
#     prefix = [0] * (len(values) + 1)

#     for i, value in enumerate(values):
#         prefix[i + 1] = prefix[i] + value

#     return prefix


# def range_sum(prefix, left, right):
#     """Return the sum of elements in the half-open interval [left, right)."""
#     return prefix[right] - prefix[left]


# def solve():
#     num_trolleys, num_days = map(int, input().split())
#     trolleys = list(map(int, input().split()))

#     # Build prefix sums once.
#     prefix = build_prefix_sum(trolleys)

#     # The original array is no longer needed.
#     del trolleys

#     # Active interval is always [left, right)
#     left = 0
#     right = num_trolleys

#     results = []

#     for _ in range(num_days):
#         split_index = int(input())

#         # Position immediately after the first split_index elements.
#         split_pos = left + split_index

#         left_sum = range_sum(prefix, left, split_pos)
#         right_sum = range_sum(prefix, split_pos, right)

#         if left_sum >= right_sum:
#             results.append(str(left_sum))
#             left = split_pos
#         else:
#             results.append(str(right_sum))
#             right = split_pos

#     sys.stdout.write("\n".join(results))


# if __name__ == "__main__":
#     solve()


# # 5. DMOJ problem avocadotrees, Avocado Trees!
# # Source: https://dmoj.ca/problem/avocadotrees
# import sys

# input = sys.stdin.readline


# def solve():
#     n, q, max_height = map(int, input().split())

#     # Build prefix sums of avocado yield, counting only eligible trees
#     # prefix[i] = total avocados from trees 1..i that are short enough to steal from
#     prefix = [0] * (n + 1)

#     for i in range(1, n + 1):
#         height, avocados = map(int, input().split())
#         eligible_yield = avocados if height <= max_height else 0
#         prefix[i] = prefix[i - 1] + eligible_yield

#     # Answer each query in O(1) using the prefix sum
#     best = 0

#     for _ in range(q):
#         left, right = map(int, input().split())
#         range_total = prefix[right] - prefix[left - 1]
#         best = max(best, range_total)

#     print(best)


# solve()


# # 6. DMOJ problem coci11c5p2, Eko (Hint: the maximum number of trees is far fewer than the maximum number of heights. Consider each tree from tallest to shortest.)
# # Source: https://dmoj.ca/problem/coci11c5p2
# import sys


# def solve():
#     # Read all input at once for maximum input performance
#     data = sys.stdin.buffer.read().split()
#     if not data:
#         return

#     n = int(data[0])
#     required_wood = int(data[1])
#     trees = list(map(int, data[2:2 + n]))

#     # Search space:
#     # The saw blade height can be anywhere from 0
#     # up to the height of the tallest tree.
#     low = 0
#     high = max(trees)

#     best_height = 0

#     while low <= high:
#         mid = (low + high) // 2

#         # Calculate how much wood would be obtained
#         # if the saw blade were set to 'mid'.
#         wood_obtained = 0

#         for tree in trees:
#             if tree > mid:
#                 wood_obtained += tree - mid

#                 # No need to continue once we've already
#                 # collected enough wood.
#                 if wood_obtained >= required_wood:
#                     break

#         if wood_obtained >= required_wood:
#             # Current height is feasible.
#             # Try a higher blade to maximize the answer.
#             best_height = mid
#             low = mid + 1
#         else:
#             # Not enough wood.
#             # Lower the blade.
#             high = mid - 1

#     print(best_height)


# if __name__ == "__main__":
#     solve()


# # 7. DMOJ problem wac6p2, Cheap Christmas Lights (Hint: don’t try flipping a switch each second—how would you know which one to flip? Instead, store them up, and use them all as soon as you can shut off all the lights that are on.)
# # Source: https://dmoj.ca/problem/wac6p2
# import sys

# input = sys.stdin.readline


# def solve():
#     n, k = map(int, input().split())
#     initial_states = list(map(int, input().split()))
#     auto_toggles   = list(map(int, input().split()))

#     net_on = sum(initial_states)

#     if net_on == 0:
#         print(0)
#         return

#     # Track which lights have been toggled an odd number of times so far.
#     # A light's current net state = initial_state XOR (has it been toggled odd times?)
#     toggled_odd_times = set()

#     for t in range(1, n + 1):

#         # Apply the auto-toggle for this second (only within the first k seconds)
#         if t <= k:
#             light = auto_toggles[t - 1]

#             is_initially_on      = initial_states[light - 1] == 1
#             is_toggled_odd_times = light in toggled_odd_times
#             is_currently_net_on  = is_initially_on ^ is_toggled_odd_times

#             if is_currently_net_on:
#                 net_on -= 1  # auto-toggle turns this light OFF
#             else:
#                 net_on += 1  # auto-toggle turns this light ON

#             # Flip the parity for this light
#             if light in toggled_odd_times:
#                 toggled_odd_times.discard(light)
#             else:
#                 toggled_odd_times.add(light)

#         # Wesley has t presses total by end of second t.
#         # If net_on <= t, he can press each net-ON light exactly once → all off.
#         if net_on <= t:
#             print(t)
#             return


# solve()

# 8. DMOJ problem ioi98p3, Party Lamps (Hint: all that matters for each button is whether it is pressed an even or odd number of times.)
# Source: https://dmoj.ca/problem/ioi98p3
import sys


def solve():
    input_func = sys.stdin.readline

    line1 = input_func().strip()
    if not line1:
        return
    n = int(line1)
    c = int(input_func().strip())

    o_n = list(map(int, input_func().split()))[:-1]
    o_f = list(map(int, input_func().split()))[:-1]

    all_combinations = []
    for b1 in range(2):
        for b2 in range(2):
            for b3 in range(2):
                for b4 in range(2):
                    all_combinations.append((b1, b2, b3, b4))

    valid_results = set()

    for b1, b2, b3, b4 in all_combinations:
        presses = b1 + b2 + b3 + b4

        if presses <= c and (c - presses) % 2 == 0:
            lamps = [1] * (n + 1)

            if b1:
                for i in range(1, n + 1):
                    lamps[i] = 1 - lamps[i]

            if b2:
                for i in range(1, n + 1):
                    if i % 2 != 0:
                        lamps[i] = 1 - lamps[i]

            if b3:
                for i in range(1, n + 1):
                    if i % 2 == 0:
                        lamps[i] = 1 - lamps[i]

            if b4:
                for i in range(1, n + 1):
                    if i % 3 == 1:
                        lamps[i] = 1 - lamps[i]

            is_valid = True

            for lamp in o_n:
                if lamps[lamp] != 1:
                    is_valid = False
                    break

            if is_valid:
                for lamp in o_f:
                    if lamps[lamp] != 0:
                        is_valid = False
                        break

            if is_valid:
                result_str = "".join(map(str, lamps[1:]))
                valid_results.add(result_str)

    if not valid_results:
        print("IMPOSSIBLE")
    else:
        for res in valid_results:
            print(res)


if __name__ == "__main__":
    solve()
