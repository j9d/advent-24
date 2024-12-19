import functools


with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()

towels = buffer[0].split(", ")
patterns = buffer[2:]

@functools.cache
def patterns_possible(pattern: str) -> int:
    if pattern == "":
        return 1
    matching = [towel for towel in towels if pattern.startswith(towel)]
    return sum([patterns_possible(pattern[len(towel):]) for towel in matching])

total = 0
for pattern in enumerate(patterns):
    total += patterns_possible(pattern)

print(total)
