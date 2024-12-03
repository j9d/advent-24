import re


with open('input.txt', 'r') as f:
    buffer = "".join(f.readlines())

pattern = r"mul\((\d{1,4}),(\d{1,4})\)"

matches: list[tuple[str, str]] = re.findall(pattern, buffer)

total = sum([int(a) * int(b) for a, b in matches])
print(total)
