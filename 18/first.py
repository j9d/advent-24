from copy import copy
from heapq import heappop, heappush

WIDTH = 71
MOVEMENT_MAP = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

Node = tuple[int, int, int, set[tuple[int, int]]]

maze = [["." for _ in range(WIDTH)] for _ in range(WIDTH)]
with open('input.txt', 'r') as f:
    for line in f.read().splitlines()[:1024]:
        x, y = line.split(",")
        maze[int(y)][int(x)] = "#"

start = (0,0)
end = (WIDTH - 1, WIDTH - 1)

def get_neighbours(score: int, row: int, col: int, trail: set[tuple[int, int]]) -> list[Node]:
    neighbours: list[Node] = []
    for row_diff, col_diff in MOVEMENT_MAP.values():
        new_row = row + row_diff
        new_col = col + col_diff
        if new_row < 0 or new_row >= len(maze) or new_col < 0 or new_col >= len(maze[new_row]):
            continue
        new_cell = maze[new_row][new_col]
        score_diff = 1
        if new_cell == ".":
            new_node = Node(
                (score + score_diff, new_row, new_col, copy(trail))
            )
            neighbours.append(new_node)
    return neighbours

def get_node(moves: list[Node], row: int, col: int) -> Node | None:
    for node in moves:
        _, node_row, node_col, _ = node
        if (node_row, node_col) == (row, col):
            return node

lowest = None
moves: list[Node] = []
visited: dict[tuple[int, int], int] = {}
heappush(moves, (0, start[0], start[1], set()))
while moves:
    score, row, col, trail = heappop(moves)
    if (row, col) in trail:
        continue
    if (row, col) in visited and visited[row, col] < score:
        continue
    if (row, col) == end:
        lowest = score
        break
    visited[row, col] = score
    trail.add((row, col))
    for neighbour in get_neighbours(score, row, col, trail):
        if get_node(moves, neighbour[1], neighbour[2]) is None:
            heappush(moves, neighbour)

print(lowest)
