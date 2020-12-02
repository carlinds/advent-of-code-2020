def main():
    with open('expenses.txt') as f:
        expenses = f.read()
        expenses = [int(x) for x in expenses.split('\n')]

    for i in expenses:
        for j in expenses:
            if (i != j) and (i + j == 2020):
                print(i*j)
                return 0

    return 1




if __name__ == '__main__':
    main()