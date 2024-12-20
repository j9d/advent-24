import functools

TO_SAVE = 100
MOVEMENT_MAP = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

with open('sample.txt', 'r') as f:
    maze = [[char for char in line] for line in f.read().splitlines()]

start = (0,0)
end = (0,0)
starting_walls: set[tuple[int, int]] = set()
spaces: dict[tuple[int, int], int] = {}

@functools.cache
def get_neighbours(row: int, col: int, return_walls: bool) -> list[tuple[int, int]]:
    neighbours: list[tuple[int, int]] = []
    for row_diff, col_diff in MOVEMENT_MAP.values():
        new_row = row + row_diff
        new_col = col + col_diff
        if new_row < 0 or new_row >= len(maze) or new_col < 0 or new_col >= len(maze[new_row]):
            continue
        new_cell = maze[new_row][new_col]
        if new_cell == "#" and return_walls:
                neighbours.append((new_row, new_col))
        if new_cell in ["S", ".", "E"] and not return_walls:
            neighbours.append((new_row, new_col))
    return neighbours

for row, line in enumerate(maze):
    for col, char in enumerate(line):
        if char == "S":
            start = (row, col)
            spaces[row, col] = -1
        if char == "E":
            end = (row, col)
            spaces[row, col] = -1
        if char == "#":
            if get_neighbours(row, col, False):
                starting_walls.add((row, col))
        if char == ".":
            spaces[row, col] = -1

dist = 0
current = start
while current != end:
    spaces[current] = dist
    dist += 1
    current = [i for i in get_neighbours(*current, False) if spaces[i] == -1][0]

spaces[end] = max(spaces.values()) + 1

shortcuts: set[tuple[tuple[int, int], tuple[int, int]]] = set()
for source_space in spaces.keys():
    neighbours = get_neighbours(*source_space, False)
    seen_spaces: set[tuple[int, int]] = set()
    seen_spaces.add(source_space)
    source_score = spaces[source_space]
    to_search: set[tuple[int, int]] = set()
    to_search.add(source_space)
    for cut_length in range(20):
        to_search_next: set[tuple[int, int]] = set()
        for current in to_search:
            neighbours = [*get_neighbours(*current, False), *get_neighbours(*current, True)]
            for row, col in neighbours:
                if maze[row][col] in [".", "E"]:
                    score = spaces[row, col]
                    if (source_score + cut_length + 1 + TO_SAVE) <= score:
                        shortcuts.add((source_space, (row, col)))
                to_search_next.add((row, col))
        seen_spaces.update(to_search)
        to_search = to_search_next

print(len(shortcuts))
