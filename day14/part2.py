from collections import*
import itertools

def main():
    with open('program.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    mem = defaultdict(int)

    for line in lines:
        a, v = line.split(' = ')
        if a == 'mask':
            mask = v
        else:
            input_pos = int(a[4:-1])
            result = int(v)
            temp_pos = 0

            floating_bits = []
            for i in range(36):
                mask_bit = mask[-1-i]
                if mask_bit == 'X':
                    floating_bits.append(1 << i)

                elif mask_bit == '1' or (input_pos & (1 << i)) > 0:
                    temp_pos += (1 << i)

            for j in range(len(floating_bits) + 1):
                for possible_combination in itertools.combinations(floating_bits, j):
                    s = sum(possible_combination)
                    mem[temp_pos + s] = result

    print(sum(mem.values()))
    return 0


if __name__ == "__main__":
    main()