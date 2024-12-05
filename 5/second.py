from functools import cmp_to_key


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

def get_applicable_rules(update: list[str]) -> list[list[str]]:
    applicable_rules: list[list[str]] = []
    for rule in rules:
        if all(item in update for item in rule):
            applicable_rules.append(rule)
    return applicable_rules

def update_is_valid(update: list[str], applicable_rules: list[list[str]]) -> bool:
    for rule in applicable_rules:
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

def fix_update(update: list[str], applicable_rules: list[list[str]]) -> list[str]:
    def sort_update(a: str, b: str) -> int:
        for rule in applicable_rules:
            if a in rule and b in rule:
                return -1 if rule[0] == a else 1
        return 0

    new_update: list[str] = sorted(update, key=cmp_to_key(sort_update))
    return new_update

for update in updates:
    applicable_rules = get_applicable_rules(update)
    if not update_is_valid(update, applicable_rules):
        fixed_update: list[str] = fix_update(update, applicable_rules)
        idx = int((len(fixed_update) - 1) / 2)
        total += int(fixed_update[idx])

print(total)
