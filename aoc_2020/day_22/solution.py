import time



def parse_decks(data):
    player_1 = []
    player_2 = []

    current_player = 1
    for line in data:
        if line == "Player 1:":
            current_player = 1
        elif line == "Player 2:":
            current_player = 2
        elif line == "":
            continue
        else:
            if current_player == 1:
                player_1.append(int(line))
            elif current_player == 2:
                player_2.append(int(line))
    return player_1, player_2


def game_result(data):
    deck_1, deck_2 = parse_decks(data)

    while len(deck_1) > 0 and len(deck_2) > 0:
        top_card_1 = deck_1.pop(0)
        top_card_2 = deck_2.pop(0)

        if top_card_1 > top_card_2: # Player 1 wins the round
            deck_1.append(top_card_1)
            deck_1.append(top_card_2)
        elif top_card_2 > top_card_1: # Player 2 wins the round
            deck_2.append(top_card_2)
            deck_2.append(top_card_1)

    winning_deck = deck_1 + deck_2

    score = 0
    value = 1

    for card in winning_deck[::-1]:
        score += card*value
        value += 1
    return score


def recursive_combat_game(deck_1, deck_2, game_count = 1):
    previous_rounds = set()

    round = 1

    while len(deck_1) > 0 and len(deck_2) > 0:
        decks = (deck_1, deck_2)
        hashed_decks = hash(decks)
        if hashed_decks in previous_rounds:
            # Game ends and Player 1 wins due to infinite game prevention rule
            deck_2 = tuple()
            print(f"The winner of game {game_count} is player 1!")
            # print(f"Player 1 wins round {round} of game {game_count}!")
            return 1, deck_1, deck_2

        previous_rounds.add(hash(decks))

        top_card_1 = deck_1[0]
        top_card_2 = deck_2[0]
        deck_1 = deck_1[1:]
        deck_2 = deck_2[1:]

        if len(deck_1) >= top_card_1 and len(deck_2) >= top_card_2:
            # New game of Recursive Combat
            winner, _, _ = recursive_combat_game(deck_1, deck_2, game_count+1)
            if winner == 1:
                deck_1 = deck_1 + (top_card_1, top_card_2)
            elif winner == 2:
                deck_2 = deck_2 + (top_card_2, top_card_1)
        else:
            # The highest card wins
            if top_card_1 > top_card_2: # Player 1 wins the round
                deck_1 = deck_1 + (top_card_1, top_card_2)
            elif top_card_2 > top_card_1: # Player 2 wins the round
                deck_2 = deck_2 + (top_card_2, top_card_1)

    if len(deck_1) == 0:
        # Player 2 wins and the game ends
        return 2, deck_1, deck_2
    elif len(deck_2) == 0:
        # Player 1 wins and the game ends
        return 1, deck_1, deck_2
    else:
        raise ValueError("Something went wrong")


def recursive_combat_result(data):
    deck_1, deck_2 = parse_decks(data)
    deck_1 = tuple(deck_1)
    deck_2 = tuple(deck_2)


    _, deck_1, deck_2 = recursive_combat_game(deck_1, deck_2) 


    # Calculate score
    winning_deck = deck_1 + deck_2
    print(f"{winning_deck=}")

    score = 0
    value = 1
    for card in winning_deck[::-1]:
        score += card*value
        value += 1
    return score



def solution_part_1():
    data = [x for x in open('input.txt').read().splitlines()]
    return game_result(data)


def solution_part_2():
    return "Not solved yet"


if __name__ == "__main__":
    print("Part 1")
    tic = time.perf_counter()
    print("- answer:", solution_part_1())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")

    print("Part 2")
    tic = time.perf_counter()
    print("- answer:", solution_part_2())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")
