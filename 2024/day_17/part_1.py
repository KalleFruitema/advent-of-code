import re


with open("2024/day_17/input.txt") as file:
    registers, program = file.read().strip().split("\n\n")
    
A, B, C = map(int, re.findall(r"-?\d+", registers.strip()))
program = list(map(int, re.findall(r"-?\d+", program.strip())))
pointer = 0
output = []


def get_combo(literal: int, A, B, C) -> int:
    if literal < 4:
        return literal
    else:
        return [A, B, C][literal - 4]


def adv(literal: int) -> None:
    global A
    combo = get_combo(literal, A, B, C)
    A = A >> combo
    

def bxl(literal: int) -> None:
    global B
    B = B ^ literal
    

def bst(literal: int) -> None:
    global B
    B = get_combo(literal, A, B, C) % 8
    
    
def jnz(literal: int) -> None:
    global pointer
    if A != 0:
        pointer = literal
        

def bxc(literal: int) -> None:
    global B
    B = B ^ C
    

def out(literal: int) -> int:
    combo = get_combo(literal, A, B, C)
    return combo % 8
    
    
def bdv(literal: int) -> None:
    global B
    combo = get_combo(literal, A, B, C)
    B = A >> combo
    
    
def cdv(literal: int) -> None:
    global C
    combo = get_combo(literal, A, B, C)
    C = A >> combo


instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


while pointer < len(program):
    operand, literal = instructions[program[pointer]], program[pointer + 1]
    pointer += 2
    result = operand(literal)
    if not result is None:
        output.append(result)
   
print(",".join(map(str, output)))