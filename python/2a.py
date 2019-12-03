import sys

with open('2.txt') as f:
    prog = list(map(int, f.read().split(',')))

prog[1] = 12
prog[2] = 2

ip = 0
while True:
    op = prog[ip]
    if op == 99:
        break
    elif op == 1:
        prog[prog[ip+3]] = prog[prog[ip+1]] + prog[prog[ip+2]]
    elif op == 2:
        prog[prog[ip+3]] = prog[prog[ip+1]] * prog[prog[ip+2]]
    else:
        print('bad opcode: ', op)
        print(prog)
        sys.exit(1)
    ip += 4

print(prog[0])
