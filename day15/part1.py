from collections import defaultdict

def main():
    with open('startingnumbers.txt') as f:
        numbers = [int(number) for number in (f.readline().strip().split(','))]

    start_length = len(numbers)
    memory = defaultdict(int)
    for i in range(1, start_length):
        memory[numbers[i-1]] = i

    for i in range(start_length, 2020):
        latest_num = numbers[i-1]

        if memory[latest_num] == 0:
            numbers.append(0)
        else:
            numbers.append(i - memory[latest_num])
        
        memory[latest_num] = i
    
    print(numbers[-1])
    return 0


if __name__ == "__main__":
    main()