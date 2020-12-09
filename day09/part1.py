from itertools import combinations

def main():
    with open('numbers.txt') as f:
        data = [int(line.strip()) for line in f.readlines()]
    
    preamble_length = 25
    for idx in range(preamble_length, len(data)):
        prev_sums = list(map(sum, combinations(data[idx-preamble_length:idx], 2)))

        if not data[idx] in prev_sums:
            print(data[idx])
            return 0
    
    return 1
    

if __name__ == "__main__":
    main()