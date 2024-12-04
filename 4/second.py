MOVEMENT_MAP = {
    "upright": (-1, 1),
    "downright": (1, 1),
    "downleft": (1, -1),
    "upleft": (-1, -1),
}

total = 0

with open('input.txt', 'r') as f:
    buffer = f.readlines()

def get_cell(row: int, col: int, movement: str) -> str:
    row_diff, col_diff = MOVEMENT_MAP[movement]
    new_row = row + row_diff
    new_col = col + col_diff

    if new_row < 0 or new_row >= len(buffer):
        return ""
    
    if new_col < 0 or new_col >= len(buffer[new_row]):
        return ""

    return buffer[new_row][new_col]

for r, row in enumerate(buffer):
    for c, col in enumerate(row):
        if col == "A":
            rising_buffer = {"M": False, "S": False}
            falling_buffer = {"M": False, "S": False}
            for movement in MOVEMENT_MAP.keys():
                new_cell = get_cell(r, c, movement)
                if new_cell in ["M", "S"]:
                    if movement in ["upright", "downleft"]:
                        rising_buffer[new_cell] = True
                    if movement in ["upleft", "downright"]:
                        falling_buffer[new_cell] = True
            if all(list(rising_buffer.values()) + list(falling_buffer.values())):
                total += 1

print(total)     
