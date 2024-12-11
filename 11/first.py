with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()[0]

stones = buffer.split(" ")

for i in range(25):
    idx = 0
    while True:
        stone = stones[idx]
        if stone == "0":
            stones[idx] = "1"
        elif len(stone) % 2 == 0:
            _ = stones.pop(idx)
            half = len(stone) // 2
            a, b = stone[:half], stone[half:]
            stones.insert(idx, str(int(a)))
            stones.insert(idx + 1, str(int(b)))
            idx += 1
        else:
            _ = stones.pop(idx)
            new = str(int(stone) * 2024)
            stones.insert(idx, new)
        idx += 1
        if idx >= len(stones):
            break

print(len(stones))
