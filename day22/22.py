with open('02.txt', 'r') as f:
    data = f.read()
    player_1_data, player_2_data = data.split('\n\n')
player_1_cards = list(map(int, player_1_data.split(':')[1].split()))
player_2_cards = list(map(int, player_2_data.split(':')[1].split()))

while player_1_cards and player_2_cards:
    card_1 = player_1_cards.pop(0)
    card_2 = player_2_cards.pop(0)
    if card_1 > card_2:
        player_1_cards.extend([card_1, card_2])
    elif card_2 > card_1:
        player_2_cards.extend([card_2, card_1])

if player_1_cards:
    winner = player_1_cards
else:
    winner = player_2_cards
total = 0
winner.reverse()
for m, c in enumerate(winner):
    total += (m+1) * c
print('Part 1:', total)

player_1_cards = list(map(int, player_1_data.split(':')[1].split()))
player_2_cards = list(map(int, player_2_data.split(':')[1].split()))


def game(p1_cards, p2_cards):
    games = set()
    while p1_cards and p2_cards:
        if (game_state := tuple(p1_cards + ['+'] + p2_cards)) in games:
            return [1], []
        else:
            games.add(game_state)

        c1 = p1_cards.pop(0)
        c2 = p2_cards.pop(0)

        if len(p1_cards) >= c1 and len(p2_cards) >= c2:
            sub1_cards, sub2_cards = game(p1_cards[:c1], p2_cards[:c2])
            if sub1_cards:
                p1_cards.extend([c1, c2])
            else:
                p2_cards.extend([c2, c1])
        elif c1 > c2:
            p1_cards.extend([c1, c2])
        elif c2 > c1:
            p2_cards.extend([c2, c1])
    return p1_cards, p2_cards


player_1_cards, player_2_cards = game(player_1_cards, player_2_cards)

if player_1_cards:
    winner = player_1_cards
else:
    winner = player_2_cards
total = 0
winner.reverse()
for m, c in enumerate(winner):
    total += (m+1) * c
print('Part 2:', total)