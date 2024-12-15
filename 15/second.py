from copy import deepcopy


MOVEMENT_MAP = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()

grid: list[list[str]] = []
moves: list[str] = []

pointer = 0
while True:
    row = buffer[pointer]
    if not row:
        break
    row_chars: list[str] = []
    for char in row:
        if char == "#":
            row_chars.extend(["#", "#"])
        elif char == "O":
            row_chars.extend(["[", "]"])
        elif char == ".":
            row_chars.extend([".", "."])
        elif char == "@":
            row_chars.extend(["@", "."])
    grid.append(row_chars)
    pointer += 1

pointer += 1
while True:
    if pointer >= len(buffer):
        break
    row = buffer[pointer]
    moves.extend([i for i in row])
    pointer += 1

def find_robot() -> tuple[int, int]:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                return row, col
    return (0, 0)

def invert_direction(direction: str) -> str:
    directions = list(MOVEMENT_MAP.keys())
    idx = directions.index(direction)
    idx = (idx + 2) % 4
    return directions[idx]

def do_move(direction: str, location: tuple[int, int]) -> tuple[int, int]:
    row, col = location
    row_diff, col_diff = MOVEMENT_MAP[direction]
    row = row + row_diff
    col = col + col_diff
    return (row, col)

def get_movable_cells_h(grid: list[list[str]], direction: str, location: tuple[int, int]) -> list[tuple[int, int]] | None:
    row, col = location
    cells: list[tuple[int, int]] = []
    while True:
        row_diff, col_diff = MOVEMENT_MAP[direction]
        row = row + row_diff
        col = col + col_diff
        cell = grid[row][col]
        if cell in ["[", "]"]:
            cells.append((row, col))
            continue
        if cell == "#":
            return None
        if cell == ".":
            return cells

def get_movable_cells_v(grid: list[list[str]], direction: str, location: tuple[int, int]) -> list[tuple[int, int]] | None:
    row, col = location
    row_diff, col_diff = MOVEMENT_MAP[direction]

    next_row = row + row_diff
    next_col = col + col_diff
    next_cell = grid[next_row][next_col]

    if next_cell == "#":
        return None
    elif next_cell == ".":
        return [(row, col)]
    elif next_cell == "[":
        space_direct = get_movable_cells_v(grid, direction, (next_row, next_col))
        space_shifted = get_movable_cells_v(grid, direction, (next_row, next_col + 1))
        if space_direct is None or space_shifted is None:
            return None
        return [(row, col), *space_direct, *space_shifted]
    elif next_cell == "]":
        space_direct = get_movable_cells_v(grid, direction, (next_row, next_col))
        space_shifted = get_movable_cells_v(grid, direction, (next_row, next_col - 1))
        if space_direct is None or space_shifted is None:
            return None
        return [(row, col), *space_direct, *space_shifted]

def process_move(
    grid: list[list[str]],
    spaces: list[tuple[int, int]],
    direction: str,
    location: tuple[int, int]
) -> tuple[list[list[str]], tuple[int, int]]:
    robot_location = do_move(direction, location)
    copy = deepcopy(grid)
    for row, col in spaces:
        copy[row][col] = "."
    for src_row, src_col in spaces:
        dest_row, dest_col = do_move(direction, (src_row, src_col))
        copy[dest_row][dest_col] = grid[src_row][src_col]
    return copy, robot_location


robot = find_robot()
grid[robot[0]][robot[1]] = "."

for idx, move in enumerate(moves):
    if move in ["<", ">"]:
        spaces = get_movable_cells_h(grid, move, robot)
    else:
        spaces = get_movable_cells_v(grid, move, robot)
    if spaces is not None:
        grid, robot = process_move(grid, list(set(spaces)), move, robot)

total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        cell = grid[row][col]
        if cell == "[":
            total += ((row * 100) + col)

print(total)
