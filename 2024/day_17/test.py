import re


class ClassicVM:
    def __init__(self, a, b, c, inst):
        self.a, self.b, self.c, self.inst = a, b, c, inst
        self.ip = 0

    def combo(self, label): return {4: self.a, 5: self.b, 6: self.c}.get(label, label)
    def adv(self, operand): self.a = self.a >> self.combo(operand)
    def bxl(self, operand): self.b = self.b ^ operand
    def bst(self, operand): self.b = self.combo(operand) & 0x07
    def bxc(self, operand): self.b = self.b ^ self.c
    def bdv(self, operand): self.b = self.a >> self.combo(operand)
    def cdv(self, operand): self.c = self.a >> self.combo(operand)
    def jnz(self, operand): self.ip = operand - 2 if self.a else self.ip
    def out(self, operand): print(self.combo(operand) & 0x07, end=',')

    def run(self):
        while self.ip < len(self.inst):
            opcode, operand = self.inst[self.ip], self.inst[self.ip + 1]
            {
                0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz,
                4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv
            }[opcode](operand)
            self.ip += 2


def task1(cnt):
    a, b, c, *inst = map(int, re.findall(r'-?\d+', cnt))
    vm = ClassicVM(a,b,c, inst)
    vm.run()


with open("2024/day_17/input.txt") as file:
    cnt = file.read()
    
task1(cnt)