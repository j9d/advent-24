from typing import TypedDict

WIDTH = 101
HEIGHT = 103
SECONDS = 100


class Guard(TypedDict):
    row: int
    col: int
    row_vel: int
    col_vel: int

def solve_guard(guard: Guard) -> tuple[int, int]:
    row = guard["row"]
    col = guard["col"]
    rv = guard["row_vel"]
    cv = guard["col_vel"]
    row = (row + (rv * SECONDS)) % HEIGHT
    col = (col + (cv * SECONDS)) % WIDTH
    return (row, col)

guards: list[Guard] = []
with open('input.txt', 'r') as f:
    for line in f.read().splitlines():
        pos, vel = line.split(" ")
        x, y = pos[2:].split(",")
        vx, vy = vel[2:].split(",")
        guard = Guard(row=int(y), col=int(x), row_vel=int(vy), col_vel=int(vx))
        guards.append(guard)

ends: list[tuple[int, int]] = []
for guard in guards:
    ends.append(solve_guard(guard))

# 0 1
# 2 3
quadrants: list[int] = [0, 0, 0, 0]
for end in ends:
    idx = None
    if end[0] < (HEIGHT // 2) and end[1] < (WIDTH // 2):
        idx = 0
    elif end[0] < (HEIGHT // 2) and end[1] > (WIDTH // 2):
        idx = 1
    elif end[0] > (HEIGHT // 2) and end[1] < (WIDTH // 2):
        idx = 2
    elif end[0] > (HEIGHT // 2) and end[1] > (WIDTH // 2):
        idx = 3
    if idx is not None:
        quadrants[idx] += 1

total = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(total)
