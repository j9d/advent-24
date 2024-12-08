import itertools


OPERATIONS = ["+", "*", "||"]

equations: list[tuple[int, list[int]]] = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        value, inputs = line.split(":")
        inputs = [int(input) for input in inputs.strip().split(" ")]
        equations.append((int(value), inputs))

def solve(inputs: list[int], operators: list[str]) -> int:
    running_total = inputs[0]
    for num, op in zip(inputs[1:], operators):
        if op == "+":
            running_total += num
        elif op == "*":
            running_total *= num
        elif op == "||":
            running_total = int(str(running_total) + str(num))
    return running_total

total = 0
for target, values in equations:
    for combo in itertools.product(OPERATIONS, repeat=(len(values) - 1)):
        res = solve(values, list(combo))
        if res == target:
            total += res
            break

print(total)
