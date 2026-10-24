from collections import deque  # noqa
from typing import List  # noqa

# 1: Source: https://neetcode.io/problems/count-number-of-islands/history?list=neetcode150&submissionIndex=0


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         """
#         Count the number of islands in a 2D grid.

#         An island is a group of land cells connected horizontally
#         or vertically.

#         Args:
#             grid: A 2D list where "1" represents land and "0" represents water.

#         Returns:
#             The total number of islands in the grid.
#         """
#         directions = {
#             "U": (-1, 0),
#             "D": (1, 0),
#             "L": (0, -1),
#             "R": (0, 1),
#         }

#         visited = set()
#         count = 0

#         def bfs(row, col):
#             """
#             Visit all land cells connected to the starting cell.

#             Args:
#                 row: The starting row index.
#                 col: The starting column index.
#             """
#             queue = deque([(row, col)])
#             visited.add((row, col))

#             while queue:
#                 current_row, current_col = queue.popleft()

#                 for dr, dc in directions.values():
#                     new_row = current_row + dr
#                     new_col = current_col + dc

#                     if (
#                         new_row < 0
#                         or new_row >= len(grid)
#                         or new_col < 0
#                         or new_col >= len(grid[new_row])
#                         or grid[new_row][new_col] == "0"
#                     ):
#                         continue

#                     if (new_row, new_col) not in visited:
#                         # Mark the cell before adding it to the queue.
#                         visited.add((new_row, new_col))
#                         queue.append((new_row, new_col))

#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if grid[row][col] == "1" and (row, col) not in visited:
#                     # A new island is found.
#                     count += 1
#                     bfs(row, col)

#         return count


# 2: Source: https://neetcode.io/problems/max-area-of-island/question?list=neetcode150


# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         """
#         Return the area of the largest island in the grid.

#         Args:
#             grid: A 2D grid where 1 represents land and 0 represents water.

#         Returns:
#             The maximum area of any connected island.
#         """
#         if not grid:
#             return 0

#         directions = {
#             "U": (-1, 0),
#             "D": (1, 0),
#             "L": (0, -1),
#             "R": (0, 1),
#         }

#         visited = set()
#         biggest = 0

#         def dfs(row: int, col: int) -> int:
#             """
#             Return the area of the island connected to the given cell.

#             Args:
#                 row: The row index of the current cell.
#                 col: The column index of the current cell.

#             Returns:
#                 The number of connected land cells.
#             """
#             # Stop if the cell is invalid, water, or already visited.
#             if (
#                 row < 0
#                 or row >= len(grid)
#                 or col < 0
#                 or col >= len(grid[row])
#                 or grid[row][col] == 0
#                 or (row, col) in visited
#             ):
#                 return 0

#             visited.add((row, col))
#             area = 1

#             # Add the area of each connected neighbor.
#             for dr, dc in directions.values():
#                 new_row = row + dr
#                 new_col = col + dc
#                 area += dfs(new_row, new_col)

#             return area

#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if grid[row][col] == 1 and (row, col) not in visited:
#                     area = dfs(row, col)
#                     biggest = max(biggest, area)

#         return biggest
