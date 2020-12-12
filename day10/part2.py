import math
import numpy as np
import collections

def main():
    with open('bag.txt') as f:
        bag = [int(line.strip()) for line in f.readlines()]
    
    sorted_bag = np.array(sorted(bag))
    sorted_bag = np.insert(sorted_bag, 0, 0)
    sorted_bag = np.append(sorted_bag, sorted_bag[-1]+3)
    diff = sorted_bag[1:] - sorted_bag[:-1]

    assert ((diff == 1) | (diff == 3)).all(), 'Difference is not 1 or 3 jolt!'

    paths = collections.Counter()
    paths[0] = 1

    for adapter in sorted_bag:
        paths[adapter + 1] += paths[adapter]
        paths[adapter + 2] += paths[adapter]
        paths[adapter + 3] += paths[adapter]

    print(paths[sorted_bag[-1]])

    return 0


if __name__ == "__main__":
    main()