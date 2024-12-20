MOVEMENT_MAP = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

with open('input.txt', 'r') as f:
    maze = [[char for char in line] for line in f.read().splitlines()]

start = (0,0)
end = (0,0)
walls: set[tuple[int, int]] = set()
spaces: dict[tuple[int, int], int] = {}

for row, line in enumerate(maze):
    for col, char in enumerate(line):
        if char == "S":
            start = (row, col)
            spaces[row, col] = -1
        if char == "E":
            end = (row, col)
            spaces[row, col] = -1
        if char == "#":
            if row not in [0, len(maze) - 1] and col not in [0, len(line) - 1]:
                walls.add((row, col))
        if char == ".":
            spaces[row, col] = -1

def get_neighbours(row: int, col: int, only_unchecked: bool) -> list[tuple[int, int]]:
    neighbours: list[tuple[int, int]] = []
    for row_diff, col_diff in MOVEMENT_MAP.values():
        new_row = row + row_diff
        new_col = col + col_diff
        new_cell = maze[new_row][new_col]
        if new_cell in ["S", ".", "E"]:
            if not only_unchecked or spaces[new_row, new_col] == -1:
                neighbours.append((new_row, new_col))
    return neighbours

dist = 0
current = start
while current != end:
    spaces[current] = dist
    dist += 1
    current = get_neighbours(*current, True)[0]
spaces[end] = max(spaces.values()) + 1

shortcuts: set[tuple[int, int]] = set()
for wall in walls:
    neighbours = get_neighbours(*wall, False)
    if len(neighbours) == 2:
        score_a = spaces[neighbours[0]]
        score_b = spaces[neighbours[1]]
        cut = abs(score_a - score_b) - 2
        if cut >= 100:
            shortcuts.add(wall)

print(len(shortcuts))
