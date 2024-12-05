with open('input.txt', 'r') as f:
    buffer = f.readlines()

total = 0
rules: list[list[str]] = []
updates: list[list[str]] = []

for line in buffer:
    if "|" in line:
        rules.append(line.strip().split("|"))
    elif "," in line:
        updates.append(line.strip().split(","))

def update_is_valid(update: list[str]):
    rules_to_apply: list[list[str]] = []
    for rule in rules:
        if all(item in update for item in rule):
            rules_to_apply.append(rule)
    for rule in rules_to_apply:
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

for update in updates:
    if update_is_valid(update):
        idx = int((len(update) - 1) / 2)
        total += int(update[idx])

print(total)