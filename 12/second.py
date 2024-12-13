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

def get_edges(row: int, col: int) -> dict[str, tuple[int, int]]:
    edges: dict[str, tuple[int, int]] = {}
    current_cell = buffer[row][col]
    for direction, diffs in MOVEMENT_MAP.items():
        row_diff, col_diff = diffs
        new_row = row + row_diff
        new_col = col + col_diff
        if new_row < 0 or new_row >= len(buffer) or new_col < 0 or new_col >= len(buffer[new_row]):
            edges[direction] = (row, col)
            continue

        new_cell = buffer[new_row][new_col]
        if new_cell != current_cell:
            edges[direction] = (row, col)
    return edges

for row in range(len(buffer)):
    for col in range(len(buffer[row])):
        if (row, col) not in explored_cells():
            region = get_region(row, col)
            regions.append(region)

total = 0
for region in regions:
    region_edges = 0
    edge_cells: dict[str, dict[int, list[int]]] = {
        "up": {},
        "right": {},
        "down": {},
        "left": {},
    }
    for row, col in region:
        cell_edges = get_edges(row, col)
        for direction, edge in cell_edges.items():
            directional = edge[0] if direction in ["up", "down"] else edge[1]
            positional = edge[1] if direction in ["up", "down"] else edge[0]
            if directional not in edge_cells[direction]:
                edge_cells[direction][directional] = []
            edge_cells[direction][directional].append(positional)
    for direction, cells in edge_cells.items():
        for directional, positionals in cells.items():
            positions = sorted(positionals)
            last = None
            for position in positions:
                if last is None:
                    region_edges += 1
                else:
                    if position > (last + 1):
                        region_edges += 1
                last = position

    area = len(region)
    total += area * region_edges

print(total)
