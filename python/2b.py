import sys

with open('2.txt') as f:
    prog = tuple(map(int, f.read().split(',')))

want = 19690720

for noun in range(100):
    for verb in range(100):
        mem = list(prog)

        mem[1] = noun
        mem[2] = verb

        ip = 0
        while True:
            op = mem[ip]
            if op == 99:
                break
            elif op == 1:
                mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
            elif op == 2:
                mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
            else:
                print('bad opcode: ', op)
                print(mem)
                sys.exit(1)
            ip += 4

        if mem[0] == want:
            print(100 * noun + verb)
            sys.exit(0)

print('not found')
