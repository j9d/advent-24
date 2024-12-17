from copy import copy
from heapq import heappop, heappush

MOVEMENT_MAP = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

Node = tuple[int, int, int, str, set[tuple[int, int]]]

with open('sample.txt', 'r') as f:
    maze = [[char for char in line] for line in f.read().splitlines()]

start = (len(maze) - 2, 1)
end = (1, len(maze[1]) - 2)

maze[start[0]][start[1]] = "."
maze[end[0]][end[1]] = "."

def invert_direction(direction: str) -> str:
    directions = list(MOVEMENT_MAP.keys())
    idx = directions.index(direction)
    idx = (idx + 2) % 4
    return directions[idx]

def get_neighbours(score: int, row: int, col: int, direction: str, trail: set[tuple[int, int]]) -> list[Node]:
    neighbours: list[Node] = []
    for next_direction, (row_diff, col_diff) in MOVEMENT_MAP.items():
        if next_direction == invert_direction(direction):
            continue
        new_row = row + row_diff
        new_col = col + col_diff
        new_cell = maze[new_row][new_col]
        score_diff = 1 if next_direction == direction else 1001
        if new_cell == ".":
            new_node = Node(
                (score + score_diff, new_row, new_col, next_direction, copy(trail))
            )
            neighbours.append(new_node)
    return neighbours

lowest = None
moves: list[Node] = []
visited: dict[tuple[int, int, str], int] = {}
seats: set[tuple[int, int]] = set()
heappush(moves, (0, start[0], start[1], "right", set()))
while moves:
    score, row, col, dir, trail = heappop(moves)
    if (row, col) in trail:
        continue
    if lowest and score > lowest:
        continue
    if (row, col, dir) in visited and visited[row, col, dir] < score:
        continue
    if (row, col) == end:
        if lowest is None or score < lowest:
            lowest = score
        seats.update(trail)
        seats.add((row, col))
        continue
    visited[row, col, dir] = score
    trail.add((row, col))
    for neighbour in get_neighbours(score, row, col, dir, trail):
        heappush(moves, neighbour)

print(len(seats))
