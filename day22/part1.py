def main():
    with open('decks.txt') as f:
        [p1, p2] = f.read().split('\n\n')

    p1 = [int(line.strip()) for line in p1.split('\n')[1:]]
    p2 = [int(line.strip()) for line in p2.split('\n')[1:]]

    while len(p1) and len(p2):
        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])

        else:
            p2.append(p2[0])
            p2.append(p1[0])

        p1.pop(0)
        p2.pop(0)

    winning_deck = p1 if len(p1) else p2
    score = 0
    for i, c in enumerate(winning_deck):
        score += c * (len(winning_deck) - i)

    print('Winner score: ', score)
    return 0


if __name__ == "__main__":
    main()