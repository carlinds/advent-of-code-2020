def main():
    with open('instructions.txt') as f:
        instructions = [line.strip().split() for line in f.readlines()]

    
    for idx, [op, arg] in enumerate(instructions):
        new_instructions = instructions[:]
        if op == 'jmp':
            new_instructions[idx] = ['nop', arg]

        if op == 'nop':
            new_instructions[idx] = ['jmp', arg]
            
        succeded, acc = run_instructions(new_instructions)
        if succeded:
            print(acc)
            break

    return 1


def run_instructions(instructions):
    visited = []
    idx = 0
    acc = 0

    while True:
        [op, arg] = instructions[idx]
        visited.append(idx)

        if op == 'acc':
            acc += int(arg)
            idx += 1

        elif op == 'jmp':
            idx += int(arg)

        elif op == 'nop':
            idx += 1

        else:
            print('Unknown instruction!')
            return False, acc

        if idx in visited:
            return False, acc

        if idx == len(instructions)-1:
            return True, acc


if __name__ == "__main__":
    main()