# 6. USACO 2018 US Open Bronze Contest problem Team Tic Tac Toe
# source : https://usaco.org/index.php?page=viewproblem2&cpid=831

import os

current_path = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(current_path, "TicTacToe.in")
out_path = os.path.join(current_path, "TicTacToe.out")

with open(in_path, "r") as file_input:
    board = [file_input.readline().strip() for _ in range(3)]

lines = []
for r in range(3):
    lines.append([board[r][0], board[r][1], board[r][2]])
for c in range(3):
    lines.append([board[0][c], board[1][c], board[2][c]])
lines.append([board[0][0], board[1][1], board[2][2]])
lines.append([board[0][2], board[1][1], board[2][0]])

individual_winners = set()
team_winners = set()

for line in lines:
    unique = set(line)
    if len(unique) == 1:
        individual_winners.add(line[0])
    elif len(unique) == 2:
        team_winners.add(frozenset(unique))

with open(out_path, "w") as file_output:
    file_output.write(str(len(individual_winners)) + "\n")
    file_output.write(str(len(team_winners)) + "\n")
