with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()

towels = buffer[0].split(", ")
patterns = buffer[2:]

def pattern_is_possible(pattern: str) -> bool:
    indexes: set[int] = set()
    indexes.add(0)
    while indexes:
        ptr = indexes.pop()
        if ptr == len(pattern):
            return True
        matching = get_matching_towels(pattern[ptr:])
        for towel in matching:
            indexes.add(ptr + len(towel))
    return False

def get_matching_towels(pattern: str):
    return [towel for towel in towels if pattern.startswith(towel)]

total = 0
for pattern in patterns:
    if pattern_is_possible(pattern):
        total += 1

print(total)
