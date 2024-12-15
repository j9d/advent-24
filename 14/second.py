from itertools import groupby
from typing import TypedDict

WIDTH = 101
HEIGHT = 103


class Guard(TypedDict):
    row: int
    col: int
    row_vel: int
    col_vel: int

def solve_guard(guard: Guard, seconds: int) -> tuple[int, int]:
    row = guard["row"]
    col = guard["col"]
    rv = guard["row_vel"]
    cv = guard["col_vel"]
    row = (row + (rv * seconds)) % HEIGHT
    col = (col + (cv * seconds)) % WIDTH
    return (row, col)

guards: list[Guard] = []
with open('input.txt', 'r') as f:
    for line in f.read().splitlines():
        pos, vel = line.split(" ")
        x, y = pos[2:].split(",")
        vx, vy = vel[2:].split(",")
        guard = Guard(row=int(y), col=int(x), row_vel=int(vy), col_vel=int(vx))
        guards.append(guard)

def visualise(ends: list[tuple[int, int]]):
    grid: list[list[str]] = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for row, col in ends:
        grid[row][col] = "*"
    print("\n".join(["".join([i for i in line]) for line in grid]))

def has_likely_tree(ends: list[tuple[int, int]]) -> bool:
    new_ends = [
        sorted(list(set(v)), key=lambda x: x[1])
        for _, v in groupby(sorted(ends, key=lambda x: x[0]), key=lambda x: x[0])
    ]
    rows = [
        [col[1] for col in row]
        for row in new_ends
    ]
    for row in rows:
        count = 0
        prev = None
        for col in row:
            if prev is None:
                prev = col
                continue
            if col == prev + 1:
                count += 1
            else:
                count = 0
            if count > 10:
                return True
            prev = col
    return False

for i in range(100_000):
    ends: list[tuple[int, int]] = []
    for guard in guards:
        ends.append(solve_guard(guard, i))
    if has_likely_tree(ends):
        print("--------------------------------------------------------------------------------")
        print(i)
        print("--------------------------------------------------------------------------------")
        visualise(ends)
