with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()[0]

stones: dict[str, int] = {}
for stone in buffer.split(" "):
    stones[stone] = 1

def add_stone(cache: dict[str, int], stone: str, count: int) -> dict[str, int]:
    if stone not in cache:
        cache[stone] = 0
    cache[stone] += count
    return cache

for i in range(75):
    cache: dict[str, int] = {}
    for stone, count in stones.items():
        if stone == "0":
            cache = add_stone(cache, "1", count)
        elif len(stone) % 2 == 0:
            half = len(stone) // 2
            a, b = str(int(stone[:half])), str(int(stone[half:]))
            cache = add_stone(cache, a, count)
            cache = add_stone(cache, b, count)
        else:
            new = str(int(stone) * 2024)
            cache = add_stone(cache, new, count)
    stones = cache

print(sum(stones.values()))
