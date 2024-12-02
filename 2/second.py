def is_safe(report: list[int]) -> bool:
    increasing = None
    prev = None
    for level in report:
        if prev is not None:
            diff = level - prev
            if diff == 0:
                return False

            if increasing is None:
                increasing = diff > 0

            if not increasing:
                diff *= -1
            
            if diff < 0 or diff > 3:
                return False

        prev = level
    return True

total = 0

with open("input.txt", "r") as f:
    buffer = f.readlines()

for line in buffer:
    report = [int(level) for level in line.split(" ")]
    variants = [report[:x] + report[x+1:] for x in range(len(report))]
    if any(is_safe(variant) for variant in variants):
        total += 1

print(total)
