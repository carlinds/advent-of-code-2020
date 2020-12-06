def main():
    with open('answers.txt') as f:
        groups = [group.split('\n') for group in f.read().split('\n\n')]
    
    s = 0
    for group in groups:
        n_people = len(group)
        answers = ''.join(group)

        for question in set(answers):
            if answers.count(question) == n_people:
                s += 1

    print(s)
    return 0


if __name__ == "__main__":
    main()