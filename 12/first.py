MOVEMENT_MAP = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()

regions: list[set[tuple[int, int]]] = []

def explored_cells() -> set[tuple[int, int]]:
    explored: set[tuple[int, int]] = set()
    explored.update(*[region for region in regions])
    return explored

def move(row: int, col: int) -> set[tuple[int, int]]:
    routes: set[tuple[int, int]] = set()
    char = buffer[row][col]
    for row_diff, col_diff in MOVEMENT_MAP.values():
        new_row = row + row_diff
        new_col = col + col_diff
        if new_row < 0 or new_row >= len(buffer) or new_col < 0 or new_col >= len(buffer[new_row]):
            continue
        space = buffer[new_row][new_col]
        if space == char:
            routes.add((new_row, new_col))
    return routes

def get_region(row: int, col: int):
    region: set[tuple[int, int]] = set()
    moves: set[tuple[int, int]] = set()
    region.add((row, col))
    moves.add((row, col))
    while True:
        new_row, new_col = moves.pop()
        new_paths = move(new_row, new_col)
        for path in new_paths:
            if path not in region:
                moves.update(new_paths)
        region.update(new_paths)
        if not moves:
            break
    return region

def find_cell_perimeter(row: int, col: int) -> int:
    perimeter = 0
    current_cell = buffer[row][col]
    for row_diff, col_diff in MOVEMENT_MAP.values():
        new_row = row + row_diff
        new_col = col + col_diff
        if new_row < 0 or new_row >= len(buffer) or new_col < 0 or new_col >= len(buffer[new_row]):
            perimeter += 1
            continue
        new_cell = buffer[new_row][new_col]
        if new_cell != current_cell:
            perimeter += 1
    return perimeter

for row in range(len(buffer)):
    for col in range(len(buffer[row])):
        if (row, col) not in explored_cells():
            region = get_region(row, col)
            regions.append(region)

total = 0
for region in regions:
    perimeter = sum([find_cell_perimeter(row, col) for row, col in region])
    area = len(region)
    total += area * perimeter

print(total)
