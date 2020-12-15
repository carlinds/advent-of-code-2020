from collections import*

def main():
    with open('program.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    mem = defaultdict(int)

    for line in lines:
        a, v = line.split(' = ')
        if a == 'mask':
            mask = v
        else:
            pos = int(a[4:-1])
            value = int(v)
            result = 0

            for i in range(36):
                mask_bit = mask[-1-i]
                if mask_bit == '1' or (mask_bit == 'X' and (value & (1 << i)) > 0):
                    result += (1 << i)

            mem[pos] = result

    print(sum(mem.values()))
    return 0


if __name__ == "__main__":
    main()