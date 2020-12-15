import collections

def main():
    with open('program.txt') as f:
        instructions = []
        for line in f.readlines():
            action, value = line.strip().split(' = ')
            instructions.append((action, value))

    #print(instructions)
    mem = {}

    for action, value in instructions:
        if action == 'mask':
            mask = value
            #print(action, ' : ', mask)

        if action.startswith('mem'):
            pos = action[4:-1]
            #print('Mem pos: ', pos)

            bvalue = format(int(value), 'b').zfill(36)
            #print('Value: ', bvalue)
 
            result = mask_value(bvalue, mask)
            #print('Result: ', result, 'Decimal: ', int(result, 2))

            mem[pos] = int(result, 2)

    print(sum(mem.values()))

    return 0


def mask_value(value, mask):
    result = []
    for vb, mb in zip(value, mask):
        if mb == '1':
            result.append('1')

        elif mb == '0':
            result.append('0')
        
        else:
            result.append(vb)

    return ''.join(result)


if __name__ == "__main__":
    main()