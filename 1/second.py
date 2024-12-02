total = 0
list1: list[int] = []
list2: list[int] = []
occurrence_map: dict[int, int] = {}

with open('input.txt', 'r') as f:
    buffer = f.readlines()

for line in buffer:
    a, b = line.split("   ")
    list1.append(int(a))
    list2.append(int(b))

for item in list2:
    if item not in occurrence_map:
        occurrence_map[item] = 0
    occurrence_map[item] += 1

for item in list1:
    occurrences = occurrence_map.get(item, 0)
    total += item * occurrences

print(total)
