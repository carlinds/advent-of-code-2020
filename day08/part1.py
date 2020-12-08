def main():
    with open('instructions.txt') as f:
        instructions = f.readlines()

    visited = []
    idx = 0
    acc = 0

    while idx not in visited:
        curr = instructions[idx]
        visited.append(idx)

        [op, arg] = curr.strip().split()
        if op == 'acc':
            acc += int(arg)
            idx += 1

        elif op == 'jmp':
            idx += int(arg)

        elif op == 'nop':
            idx += 1

    print(acc)
    return 1


if __name__ == "__main__":
    main()