MOVEMENT_MAP = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()

topo_map = [[int(char) for char in line] for line in buffer]

trailheads: list[tuple[int, int]] = []

for row, line in enumerate(topo_map):
    for col, num in enumerate(line):
        if num == 0:
            trailheads.append((row, col))

def move(num: int, row: int, col: int) -> list[tuple[int, int]]:
    routes: list[tuple[int, int]] = []
    for row_diff, col_diff in MOVEMENT_MAP.values():
        new_row = row + row_diff
        new_col = col + col_diff
        if new_row < 0 or new_row >= len(buffer) or new_col < 0 or new_col >= len(buffer[new_row]):
            continue
        space = topo_map[new_row][new_col]
        if space == num + 1:
            routes.append((new_row, new_col))
    return routes

def check_trail(trailhead: tuple[int, int]) -> int:
    nines: set[tuple[int, int]] = set()
    row, col = trailhead
    moves = move(0, row, col)
    for i in range(1,9):
        cache: list[tuple[int, int]] = []
        for new_row, new_col in moves:
            new_paths = move(i, new_row, new_col)
            cache.extend(new_paths)
        if len(cache) == 0:
            return 0
        moves = [j for j in cache]
    for end in moves:
        nines.add(end)
    return len(nines)

total = 0
for trailhead in trailheads:
    score = check_trail(trailhead)
    total += score

print(total)
