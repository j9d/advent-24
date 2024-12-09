import itertools


with open('input.txt', 'r') as f:
    antenna_map = [l.strip() for l in f.readlines()]
antinode_map = [["." for _ in range(len(antenna_map[0]))] for _ in range(len(antenna_map))]

antennas: dict[str, list[tuple[int, int]]] = {}

for row, line in enumerate(antenna_map):
    for col, char in enumerate(line):
        if char != ".":
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((row, col))

for locations in antennas.values():
    combos = itertools.permutations(locations, 2)
    for a, b in combos:
        row_diff = a[0] - b[0]
        col_diff = a[1] - b[1]
        row = a[0] + row_diff
        col = a[1] + col_diff
        if row < 0 or col < 0 or row >= len(antinode_map) or col >= len(antinode_map[row]):
            continue
        antinode_map[row][col] = "#"

total = sum([line.count("#") for line in antinode_map])
print(total)
