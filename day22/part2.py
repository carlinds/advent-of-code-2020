import copy

def play_game(p1, p2):
    previous_rounds = []

    def complete_round(p1_won_round):
        if p1_won_round:
            p1.append(p1[0])
            p1.append(p2[0])
            
        else:
            p2.append(p2[0])
            p2.append(p1[0])

        p1.pop(0)
        p2.pop(0)

    while True:
        if (p1, p2) in previous_rounds:
            p1_won = True
            break

        if len(p1) == 0:
            p1_won = False
            break

        if len(p2) == 0:
            p1_won = True
            break

        else:
            previous_rounds.append((copy.deepcopy(p1), copy.deepcopy(p2)))

        if ((len(p1) - 1) >= p1[0]) and ((len(p2) - 1) >= p2[0]):
            p1_sub = copy.deepcopy(p1[1:p1[0]+1])
            p2_sub = copy.deepcopy(p2[1:p2[0]+1])
            p1_won_round = play_game(p1_sub, p2_sub)
            complete_round(p1_won_round)

        else:
            p1_won_round = p1[0] > p2[0]
            complete_round(p1_won_round)

    return p1_won

def main():
    with open('decks.txt') as f:
        [p1, p2] = f.read().split('\n\n')

    p1 = [int(line.strip()) for line in p1.split('\n')[1:]]
    p2 = [int(line.strip()) for line in p2.split('\n')[1:]]
    
    p1_won = play_game(p1, p2)
    winning_deck = p1 if p1_won else p2
    score = 0
    for i, c in enumerate(winning_deck):
        score += c * (len(winning_deck) - i)

    print('Winner score: ', score)
    return 0


if __name__ == "__main__":
    main()
    