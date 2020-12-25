from collections import defaultdict


def p1():
    player1 = []
    player2 = []

    is_p2_card = False

    with open('input.txt') as fp:
        fp.readline()
        line = fp.readline()
        while line:
            line = line[:-1]
            if line == '':
                line = fp.readline()
                continue
            if line[0] == 'P':
                line = fp.readline()
                is_p2_card = True
                continue

            if is_p2_card:
                player2.append(int(line))
            else:
                player1.append(int(line))

            line = fp.readline()

    while min(len(player1), len(player2)) != 0:
        p1_value = player1.pop(0)
        p2_value = player2.pop(0)

        if p2_value < p1_value:
            player1.append(p1_value)
            player1.append(p2_value)
        else:
            player2.append(p2_value)
            player2.append(p1_value)

    total = 0
    for idx, s in enumerate(player1):
        total += (len(player1) - idx) * s

    for idx, s in enumerate(player2):
        total += (len(player2) - idx) * s

    print(total)


def p2():
    player1 = []
    player2 = []

    is_p2_card = False

    with open('input.txt') as fp:
        fp.readline()
        line = fp.readline()
        while line:
            line = line[:-1]
            if line == '':
                line = fp.readline()
                continue
            if line[0] == 'P':
                line = fp.readline()
                is_p2_card = True
                continue

            if is_p2_card:
                player2.append(int(line))
            else:
                player1.append(int(line))

            line = fp.readline()

    def compare(player1_deck, player2_deck):
        history_set = set()
        while True:
            if min(len(player1_deck), len(player2_deck)) == 0:
                if len(player1_deck) > len(player2_deck):
                    return 1
                else:
                    return 2
            player1_deck_str = [str(e) for e in player1_deck]
            player2_deck_str = [str(e) for e in player2_deck]
            p1_record = '-'.join(player1_deck_str)
            p2_record = '-'.join(player2_deck_str)
            history = f'{p1_record}v{p2_record}'
            if history not in history_set:
                history_set.add(history)
            else:
                return 1
            # print(f'Player 1\'s deck: {player1_deck}')
            # print(f'Player 2\'s deck: {player2_deck}')
            p1_value = player1_deck.pop(0)
            p2_value = player2_deck.pop(0)

            # print(f'Player 1 plays: {p1_value}')
            # print(f'Player 2 plays: {p2_value}')

            if p1_value <= len(player1_deck) and p2_value <= len(player2_deck):  # play subgame
                # print('Playing a sub-game to determine the winner...')
                winner = compare(player1_deck[:p1_value].copy(), player2_deck[:p2_value].copy())
                if winner == 1:
                    player1_deck.append(p1_value)
                    player1_deck.append(p2_value)
                else:
                    player2_deck.append(p2_value)
                    player2_deck.append(p1_value)
            else:
                if p2_value < p1_value:
                    # print('Player 1 wins.')
                    player1_deck.append(p1_value)
                    player1_deck.append(p2_value)
                else:
                    # print('Player 2 wins.')
                    player2_deck.append(p2_value)
                    player2_deck.append(p1_value)

    win_player = compare(player1, player2)
    total = 0
    if win_player == 1:
        for idx, s in enumerate(player1):
            total += (len(player1) - idx) * s
    else:
        for idx, s in enumerate(player2):
            total += (len(player2) - idx) * s

    print(total)


if __name__ == '__main__':
    # p1()
    p2()
