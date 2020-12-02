def main():
    with open('expenses.txt') as f:
        expenses = f.read()
        expenses = [int(x) for x in expenses.split('\n')]

    expenses = sorted(expenses)
    arr_len = len(expenses)
    for i in range(arr_len):

        j = i + 1
        k = arr_len - 1

        while (j < k):
            s = expenses[i] + expenses[j] + expenses[k]
            
            if s == 2020:
                print(expenses[i] * expenses[j] * expenses[k])
                return 0
            
            elif s < 2020:
                j += 1

            else:
                k -= 1
    return 1


if __name__ == '__main__':
    main()