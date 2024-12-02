total = 0
list1: list[int] = []
list2: list[int] = []

with open('input.txt', 'r') as f:
    buffer = f.readlines()

for line in buffer:
    a, b = line.split("   ")
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

for a, b in zip(list1, list2):
    total += abs(a - b)

print(total)
