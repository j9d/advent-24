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

forward = 0
backward = len(expanded) - 1
while backward > forward:
    if expanded[forward] is None:
        if expanded[backward] is not None:
            expanded[forward] = expanded[backward]
            expanded[backward] = None
            forward += 1
        backward -= 1
    else:
        forward += 1

total = 0
for idx, val in enumerate(expanded):
    if val is None:
        break
    total += idx * val

print(total)
