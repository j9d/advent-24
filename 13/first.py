from typing import TypedDict


class Game(TypedDict):
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]

with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()

games: list[Game] = []
for line in buffer:
    if line == "":
        continue

    if line.startswith("Button A"):
        games.append({
            "a": tuple(),
            "b": tuple(),
            "prize": tuple(),
        })
    game = games[-1]
    description, info = line.split(":")
    clean_info = info.strip().split(", ")
    if description == "Button A":
        x = int(clean_info[0].split("+")[1])
        y = int(clean_info[1].split("+")[1])
        game["a"] = (x, y)
    elif description == "Button B":
        x = int(clean_info[0].split("+")[1])
        y = int(clean_info[1].split("+")[1])
        game["b"] = (x, y)
    else:
        x = int(clean_info[0].split("=")[1])
        y = int(clean_info[1].split("=")[1])
        game["prize"] = (x, y)

def get_cost(a: int, b: int) -> int:
    return (a * 3) + b

def solve_game(game: Game) -> int:
    x_factors = [game["a"][0], game["b"][0]]
    y_factors = [game["a"][1], game["b"][1]]
    x_target, y_target = game["prize"]

    x_possibilities: list[tuple[int, int]] = []
    x1_max = x_target // x_factors[0]
    x2_max = x_target // x_factors[1]
    for x1 in range(x1_max + 1):
        for x2 in range(x2_max + 1):
            if (x_factors[0] * x1) + (x_factors[1] * x2) == x_target:
                x_possibilities.append((x1, x2))

    y_possibilities: list[tuple[int, int]] = []
    y1_max = y_target // y_factors[0]
    y2_max = y_target // y_factors[1]
    for y1 in range(y1_max + 1):
        for y2 in range(y2_max + 1):
            if (y_factors[0] * y1) + (y_factors[1] * y2) == y_target:
                combo = (y1, y2)
                if combo in x_possibilities:
                    y_possibilities.append(combo)

    if not y_possibilities:
        return 0
    return min([get_cost(a, b) for a, b in y_possibilities])


total = 0
for game in games:
    cost = solve_game(game)
    total += cost

print(total)
