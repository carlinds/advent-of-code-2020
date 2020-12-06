def main():
    with open('answers.txt') as f:
        groups = [group.replace('\n','') for group in f.read().split('\n\n')]
    
    s = 0
    for group in groups:
        s += len(set(group))
    
    print(s)
    return 0


if __name__ == "__main__":
    main()