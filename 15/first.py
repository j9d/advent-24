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
    grid.append([i for i in row])
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

def do_move(direction: str, location: tuple[int, int]) -> tuple[int, int]:
    row, col = location
    row_diff, col_diff = MOVEMENT_MAP[direction]
    row = row + row_diff
    col = col + col_diff
    return (row, col)

def can_move(grid: list[list[str]], direction: str, location: tuple[int, int]) -> tuple[int, int] | None:
    row, col = location
    while True:
        row_diff, col_diff = MOVEMENT_MAP[direction]
        row = row + row_diff
        col = col + col_diff
        cell = grid[row][col]
        if cell == "#":
            return None
        if cell == ".":
            return (row, col)

def process_move(
    grid: list[list[str]],
    space: tuple[int, int],
    direction: str,
    location: tuple[int, int]
) -> tuple[list[list[str]], tuple[int, int]]:
    location = do_move(direction, location)
    robot_location = location
    grid[location[0]][location[1]] = "."
    while location != space:
        location = do_move(direction, location)
        grid[location[0]][location[1]] = "O"
    return grid, robot_location

robot = find_robot()
grid[robot[0]][robot[1]] = "."

for idx, move in enumerate(moves):
    space = can_move(grid, move, robot)
    if space:
        grid, robot = process_move(grid, space, move, robot)

total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        cell = grid[row][col]
        if cell == "O":
            total += (row * 100) + col

print(total)
