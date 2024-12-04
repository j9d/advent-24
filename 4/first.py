MOVEMENT_MAP = {
    "up": (-1, 0),
    "upright": (-1, 1),
    "right": (0, 1),
    "downright": (1, 1),
    "down": (1, 0),
    "downleft": (1, -1),
    "left": (0, -1),
    "upleft": (-1, -1),
}

total = 0

with open('input.txt', 'r') as f:
    buffer = f.readlines()

def get_cell(row: int, col: int, movement: str) -> tuple[str, int, int]:
    row_diff, col_diff = MOVEMENT_MAP[movement]
    new_row = row + row_diff
    new_col = col + col_diff

    if new_row < 0 or new_row >= len(buffer):
        return ("", row, col)
    
    if new_col < 0 or new_col >= len(buffer[new_row]):
        return ("", row, col)

    return (buffer[new_row][new_col], new_row, new_col)

for r, row in enumerate(buffer):
    for c, col in enumerate(row):
        if col == "X":
            for movement in MOVEMENT_MAP.keys():
                count = 0
                current_r = r
                current_c = c
                for target in "MAS":
                    cell, new_row, new_col = get_cell(current_r, current_c, movement)
                    if not cell or cell != target:
                        break
                    count += 1
                    current_r = new_row
                    current_c = new_col
                if count == 3:
                    total += 1

print(total)     
