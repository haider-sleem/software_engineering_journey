# # 1. USACO 2019 January Bronze Contest problem Shell Game
# # Source: https://usaco.org/index.php?page=viewproblem2&cpid=891
# n = int(input())

# moves = []

# for _ in range(n):
#     a, b, g = map(int, input().split())
#     moves.append([a, b, g])

# best_score = 0

# for start in range(1, 4):
#     pebble = start
#     score = 0

#     for a, b, g in moves:
#         if pebble == a:
#             pebble = b
#         elif pebble == b:
#             pebble = a

#         if pebble == g:
#             score += 1

#     if score > best_score:
#         best_score = score

# print(best_score)

# # 2. USACO 2016 US Open Bronze Contest problem Diamond Collector
# # Source: https://usaco.org/index.php?page=viewproblem2&cpid=639
# n, k = map(int, input().split())

# sizes = []
# for _ in range(n):
#     sizes.append(int(input()))

# sizes.sort()

# best = 0

# for i in range(n):
#     count = 0

#     for j in range(i, n):
#         if sizes[j] - sizes[i] <= k:
#             count += 1
#         else:
#             break

#     best = max(best, count)

# print(best)


# # 3. DMOJ problem coci20c1p1, Patkice
# # Source: https://dmoj.ca/problem/coci20c1p1
# import sys
# input = sys.stdin.readline

# R, C = map(int, input().split())
# grid = [input().strip() for _ in range(R)]

# for r in range(R):
#     for c in range(C):
#         if grid[r][c] == 'o':
#             sr, sc = r, c

# dirs = {'N': (-1,0), 'E': (0,1), 'S': (1,0), 'W': (0,-1)}
# current_dir = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}

# best_steps = None
# best_dir   = None

# for d in sorted(dirs):  # أبجدياً: E N S W
#     dr, dc = dirs[d]
#     r, c = sr + dr, sc + dc
#     steps = 1

#     while 0 <= r < R and 0 <= c < C:
#         cell = grid[r][c]
#         if cell == 'x':
#             if best_steps is None or steps < best_steps:
#                 best_steps = steps
#                 best_dir   = d
#             break
#         elif cell in current_dir:
#             mr, mc = current_dir[cell]
#             r += mr
#             c += mc
#             steps += 1
#         else:
#             break

# if best_dir is None:
#     print(":(")
# else:
#     print(":)")
#     print(best_dir)


# # 4. DMOJ problem ccc09j2, Old Fishin’ Hole
# # Source: https://dmoj.ca/problem/ccc09j2
# import sys
# input = sys.stdin.readline

# trout_pts    = int(input())
# pike_pts     = int(input())
# pickerel_pts = int(input())
# total        = int(input())

# results = []

# for t in range(total // trout_pts + 1):
#     for p in range((total - t * trout_pts) // pike_pts + 1):
#         for y in range((total - t * trout_pts - p * pike_pts) // pickerel_pts + 1):
#             points = t * trout_pts + p * pike_pts + y * pickerel_pts
#             if 1 <= points <= total:
#                 results.append((t, p, y))

# for t, p, y in results:
#     print(f"{t} Brown Trout, {p} Northern Pike, {y} Yellow Pickerel")

# print(f"Number of ways to catch fish: {len(results)}")


# # 5. DMOJ problem ecoo16r1p2, Spindie
# # Source: https://dmoj.ca/problem/ecoo16r1p2
# import sys

# def get_possible_scores(spinner):
#     spinner_set = set(spinner)

#     after_roll1 = set()
#     for v in spinner_set:
#         for s2 in spinner_set:
#             after_roll1.add(v + s2)
#             after_roll1.add(v * s2)

#     after_roll2 = set()
#     for v in after_roll1:
#         for s3 in spinner_set:
#             after_roll2.add(v + s3)
#             after_roll2.add(v * s3)

#     return after_roll2

# lines = sys.stdin.read().split('\n')
# idx = 0

# while idx < len(lines):
#     line = lines[idx].strip()
#     if not line:
#         idx += 1
#         continue
#     n = int(line); idx += 1
#     spinner = list(map(int, lines[idx].split())); idx += 1
#     targets = list(map(int, lines[idx].split())); idx += 1
#     possible = get_possible_scores(spinner)
#     print(''.join('T' if t in possible else 'F' for t in targets))


# # 6. DMOJ problem cco96p2, SafeBreaker
# # Source: https://dmoj.ca/problem/cco96p2
# import sys
# from collections import Counter
# input = sys.stdin.readline

# def check(secret, guess, correct, misplaced):
#     c = sum(s == g for s, g in zip(secret, guess))
#     if c != correct:
#         return False
#     s_count = Counter(s for s, g in zip(secret, guess) if s != g)
#     g_count = Counter(g for s, g in zip(secret, guess) if s != g)
#     m = sum(min(s_count[d], g_count[d]) for d in g_count)
#     return m == misplaced

# def solve(guesses):
#     valid = []
#     for code in range(10000):
#         secret = f"{code:04d}"
#         if all(check(secret, g, c, m) for g, c, m in guesses):
#             valid.append(secret)
#         if len(valid) > 1:
#             return "indeterminate"
#     if len(valid) == 0:
#         return "impossible"
#     return valid[0]

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     guesses = []
#     for _ in range(n):
#         line = input().split()
#         guess = line[0]
#         c, m = map(int, line[1].split('/'))
#         guesses.append((guess, c, m))
#     print(solve(guesses))




# # 7. USACO 2019 December Bronze Contest problem Where Am I
# # Source: https://usaco.org/index.php?page=viewproblem2&cpid=964
# n = int(input())
# s = input().strip()

# for k in range(1, n + 1):
#     seen = set()
#     unique = True

#     for i in range(n - k + 1):
#         sub = s[i:i + k]

#         if sub in seen:
#             unique = False
#             break

#         seen.add(sub)

#     if unique:
#         print(k)
#         break



# # 8. USACO 2016 January Bronze Contest problem Angry Cows
# # Source : https://usaco.org/index.php?page=viewproblem2&cpid=592
# n = int(input())
# bales = [int(input()) for _ in range(n)]

# bales.sort()

# best = 1

# for start in range(n):
#     total = 1

#     # Go left
#     current = start
#     radius = 1

#     while True:
#         next_bale = -1

#         for i in range(current - 1, -1, -1):
#             if bales[current] - bales[i] <= radius:
#                 next_bale = i
#             else:
#                 break

#         if next_bale == -1:
#             break

#         total += current - next_bale
#         current = next_bale
#         radius += 1

#     # Go right
#     current = start
#     radius = 1

#     while True:
#         next_bale = -1

#         for i in range(current + 1, n):
#             if bales[i] - bales[current] <= radius:
#                 next_bale = i
#             else:
#                 break

#         if next_bale == -1:
#             break

#         total += next_bale - current
#         current = next_bale
#         radius += 1

#     best = max(best, total)

# print(best)

"""
import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path  = os.path.join(current_path, "angry.in")
out_path = os.path.join(current_path, "angry.out")

with open(in_path, "r") as file_input:
    n = int(file_input.readline())
    bales = [int(file_input.readline()) for _ in range(n)]

best = 0

for start in bales:
    exploded = {start}
    queue = [(start, 1)]
    head = 0

    while head < len(queue):
        pos, radius = queue[head]
        head += 1
        for b in bales:
            if b not in exploded and abs(b - pos) <= radius:
                exploded.add(b)
                queue.append((b, radius + 1))

    best = max(best, len(exploded))

with open(out_path, "w") as file_output:
    file_output.write(str(best) + "\n")
"""


# # 9. USACO 2016 December Silver Contest problem Counting Haybales
# # Source: https://usaco.org/index.php?page=viewproblem2&cpid=666
# from bisect import bisect_left, bisect_right

# n, q = map(int, input().split())

# bales = list(map(int, input().split()))
# bales.sort()

# for _ in range(q):
#     a, b = map(int, input().split())

#     left = bisect_left(bales, a)
#     right = bisect_right(bales, b)

#     print(right - left)
    

# # 10. DMOJ problem crci06p3, Firefly
# # Source: https://dmoj.ca/problem/crci06p3
# import sys
# from bisect import bisect_left

# input = sys.stdin.readline

# N, H = map(int, input().split())

# bottom = []
# top = []

# for i in range(N):
#     x = int(input())
#     if i % 2 == 0:
#         bottom.append(x)
#     else:
#         top.append(x)

# bottom.sort()
# top.sort()

# best = N
# count = 0

# for level in range(1, H + 1):

#     hit_bottom = len(bottom) - bisect_left(bottom, level)

#     need = H - level + 1
#     hit_top = len(top) - bisect_left(top, need)

#     total = hit_bottom + hit_top

#     if total < best:
#         best = total
#         count = 1
#     elif total == best:
#         count += 1

# print(best, count)

"""
import sys

def solve():
    # Fast input reading
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    N = int(data[0])  # Number of obstacles (even)
    H = int(data[1])  # Cave height
    
    # Difference array: size H+2 to safely handle boundaries
    diff = [0] * (H + 2)
    
    # Process each obstacle
    idx = 2
    for i in range(N):
        size = int(data[idx])
        idx += 1
        
        if i % 2 == 0:  # Stalagmite (from floor) - positions: 0, 2, 4...
            # Affects levels 1 to size
            diff[1] += 1
            if size + 1 <= H:
                diff[size + 1] -= 1
        else:  # Stalactite (from ceiling) - positions: 1, 3, 5...
            # Affects levels (H - size + 1) to H
            start = H - size + 1
            diff[start] += 1
            diff[H + 1] -= 1  # Safe boundary marker
    
    # Calculate prefix sum and find minimum
    min_obstacles = N + 1  # Start with maximum possible + 1
    count_levels = 0
    current = 0
    
    for level in range(1, H + 1):
        current += diff[level]
        
        if current < min_obstacles:
            min_obstacles = current
            count_levels = 1
        elif current == min_obstacles:
            count_levels += 1
    
    # Output result
    print(f"{min_obstacles} {count_levels}")

if __name__ == "__main__":
    solve()
 """