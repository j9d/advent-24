with open('input.txt', 'r') as f:
    buffer = f.read().splitlines()

a = int(buffer[0].split(" ")[2])
b = int(buffer[1].split(" ")[2])
c = int(buffer[2].split(" ")[2])
program = [int(op) for op in buffer[4].split(" ")[1].split(",")]
ptr = 0
output: list[str] = []

def get_combo(operand: int) -> int:
    global a, b, c
    if operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    return -1

def adv(lit: int):
    global a
    com = get_combo(lit)
    denom: int = 2 ** com
    result = a // denom
    a = result

def bxl(lit: int):
    global b
    result = b ^ lit
    b = result

def bst(lit: int):
    global b
    com = get_combo(lit)
    result = com % 8
    b = result

def jnz(lit: int):
    global a
    global ptr
    if not a:
        return
    ptr = lit - 2

def bxc(_: int):
    global b, c
    result = b ^ c
    b = result

def out(lit: int):
    global output
    com = get_combo(lit)
    result = com % 8
    output.append(str(result))

def bdv(lit: int):
    global a, b
    com = get_combo(lit)
    denom: int = 2 ** com
    result = a // denom
    b = result

def cdv(lit: int):
    global a, c
    com = get_combo(lit)
    denom: int = 2 ** com
    result = a // denom
    c = result

INSTRUCTIONS = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
S = ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"]

try:
    while True:
        opcode = program[ptr]
        fn = INSTRUCTIONS[opcode]
        lit = program[ptr + 1]
        fn(lit)
        ptr += 2
except IndexError:
    pass

print(",".join(output))
