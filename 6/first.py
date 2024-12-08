MOVEMENT_MAP = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

row = 0
col = 0
movement = "up"

guard_map: list[list[str]] = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        line_arr: list[str] = []
        for j, char in enumerate(line.strip()):
            if char == "^":
                row = i
                col = j
                char = "X"
            line_arr.append(char)
        guard_map.append(line_arr)

def cycle_movement(current_movement: str) -> str:
    movements = list(MOVEMENT_MAP.keys())
    idx = movements.index(current_movement)
    return movements[(idx + 1) % 4]

while True:
    row_diff, col_diff = MOVEMENT_MAP[movement]
    new_row = row + row_diff
    new_col = col + col_diff

    if new_row < 0 or new_row >= len(guard_map) or new_col < 0 or new_col >= len(guard_map):
        break
    elif guard_map[new_row][new_col] == "#":
        movement = cycle_movement(movement)
        row_diff, col_diff = MOVEMENT_MAP[movement]
        new_row = row + row_diff
        new_col = col + col_diff

    guard_map[new_row][new_col] = "X"
    row = new_row
    col = new_col

total = 0
for line in guard_map:
    total += line.count("X")
print(total)
