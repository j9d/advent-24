import re


with open('input.txt', 'r') as f:
    buffer = "".join(f.readlines())

pattern = r"(do\(\))|(don\'t\(\))|(mul)\((\d{1,4}),(\d{1,4})\)"
matches: list[tuple[str, str, str, str, str]] = re.findall(pattern, buffer)

valid_ops: list[tuple[int, int]] = []
enabled = True
for match in matches:
    if "don't()" in match:
        enabled = False

    if "do()" in match:
        enabled = True

    if "mul" in match and enabled:
        valid_ops.append((int(match[3]), int(match[4])))

total = sum([a * b for a, b in valid_ops])
print(total)
