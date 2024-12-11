with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()[0]

blocks = buffer[::2]
spaces = buffer[1::2] + "0"

expanded: list[int | None] = []

for idx, info in enumerate(zip(blocks, spaces)):
    block, space = info
    for i in range(int(block)):
        expanded.append(idx)
    for i in range(int(space)):
        expanded.append(None)

def find_space(length: int, limit_idx: int) -> tuple[int, int] | None:
    start = None
    count = 0
    for idx in range(limit_idx):
        num = expanded[idx]
        if num == None:
            if start is None:
                start = idx
            count += 1
            if count == length:
                return start, idx
        else:
            start = None
            count = 0
    return None

def get_block(end_idx: int) -> tuple[int, int, int] | None:
    num = expanded[end_idx]
    if num is None:
        return None
    idx = end_idx
    while idx > 0:
        idx -= 1
        if expanded[idx] != num:
            return num, idx + 1, end_idx

forward = 0
backward = len(expanded)
while backward > 0:
    backward -= 1
    block = get_block(backward)
    if block is None:
        continue
    id, block_start, block_end = block
    block_length = (block_end - block_start) + 1
    space = find_space(block_length, backward)
    if space is None:
        backward = block_start
        continue
    space_start, space_end = space
    space_length = (space_end - space_start) + 1
    for i in range(block_length):
        curr = space_start + i
        expanded[curr] = expanded[block_start + i]
        expanded[block_start + i] = None

    backward = block_start

total = 0
for idx, val in enumerate(expanded):
    if val is not None:
        total += idx * val

print(total)
