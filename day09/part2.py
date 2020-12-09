from itertools import combinations

def main():
    with open('numbers.txt') as f:
        data = [int(line.strip()) for line in f.readlines()]
    
    preamble_length = 25
    for idx in range(preamble_length, len(data)):
        prev_sums = list(map(sum, combinations(data[idx-preamble_length:idx], 2)))

        if not data[idx] in prev_sums:
            invalid_number = data[idx]
            print('Invalid number: ', invalid_number)
            
            # Only look at data up until the invalid number
            data_subset = data[:idx]

            for window_len in range(2, len(data_subset)):
                contiguous_numbers = contiguous_set(data_subset, window_len)
                contiguous_sums = list(map(sum, contiguous_numbers))

                if invalid_number in contiguous_sums:
                    encrypyion_set = contiguous_numbers[contiguous_sums.index(invalid_number)]
                    encryption_weakness = min(encrypyion_set) + max(encrypyion_set)
                    print('Encryption weakness: ', encryption_weakness)
                    return 0
    
    return 1
    

def contiguous_set(data, length):
    slices = []
    for i in range(len(data) - length - 1):
        slices.append(data[i:i + length])
    return slices


if __name__ == "__main__":
    main()