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
        x = int(clean_info[0].split("=")[1]) + 10000000000000
        y = int(clean_info[1].split("=")[1]) + 10000000000000
        game["prize"] = (x, y)

def get_cost(a: int, b: int) -> int:
    return (a * 3) + b

def solve_game(game: Game) -> int:
    i = game["a"][0]
    j = game["b"][0]
    k = game["a"][1]
    l = game["b"][1]
    n = game["prize"][0]
    m = game["prize"][1]

    a_presses = ((l * n) - (j * m)) / ((i * l) - (j * k))
    b_presses = (m - (k * a_presses)) / l

    if (a_presses % 1 == 0) and (b_presses % 1 == 0):
        return get_cost(int(a_presses), int(b_presses))
    return 0


total = 0
for idx, game in enumerate(games):
    cost = solve_game(game)
    total += cost

print(total)
