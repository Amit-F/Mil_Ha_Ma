# to-do:
# 1. fix "1 points" bug
# 2. find a way to make the game end when 1 player reaches 0 cards
# 3. make code more efficient (loop all appends + removes)
    # a. use list comprehensions!
# 4. for multiplayer, make for loop that adds empty lists to master list and work on indices
# 5. in order for mp to work, need to loop player names
    # a. mp logic would need to include double/triple/etc milhamot, so probably not realistic
#        to pursue at this point in time

import random

class Players:

    points = 0
    cards = []
    card_values = []

    def __init__(self, name, cards, card_values, points):
        self.name = name
        self.cards = cards
        self.card_values = card_values
        self.points = points

    def set_cards_and_values(self, cards, card_values):
        self.cards = cards
        self.card_values = card_values


    def update_cards_and_values(self, cards, card_values, add_cards):  # todo check if correct (emph on .remove)
        # inputs are lists to either append or remove
        if add_cards:
            self.cards.extend(cards)
            self.card_values.extend(card_values)
            #  for i in range(len(cards)):
            #      self.cards.append(cards[i])
            #      self.card_values.append(card_values[i])
        else:
            for i in range(len(cards)):
                self.cards.remove(cards[i])
                self.card_values.remove(card_values[i])


cards = {'As': '🂡', '2s': '🂢', '3s': '🂣', '4s': '🂤', '5s': '🂥', '6s': '🂦', '7s': '🂧', '8s': '🂨', '9s': '🂩', '10s': '🂪',
         'Js': '🂫', 'Qs': '🂭', 'Ks': '🂮', 'Ah': '🂱', '2h': '🂲', '3h': '🂳', '4h': '🂴', '5h': '🂵', '6h': '🂶', '7h': '🂷',
         '8h': '🂸', '9h': '🂹', '10h': '🂺', 'Jh': '🂻', 'Qh': '🂽', 'Kh': '🂾', 'Ad': '🃁', '2d': '🃂', '3d': '🃃', '4d': '🃄',
         '5d': '🃅', '6d': '🃆', '7d': '🃇', '8d': '🃈', '9d': '🃉', '10d': '🃊', 'Jd': '🃋', 'Qd': '🃍', 'Kd': '🃎', 'Ac': '🃑',
         '2c': '🃒', '3c': '🃓', '4c': '🃔', '5c': '🃕', '6c': '🃖', '7c': '🃗', '8c': '🃘', '9c': '🃙', '10c': '🃚', 'Jc': '🃛',
         'Qc': '🃝', 'Kc': '🃞'}

values = {'🂡': 14, '🂢': 2, '🂣': 3, '🂤': 4, '🂥': 5, '🂦': 6, '🂧': 7, '🂨': 8, '🂩': 9, '🂪': 10, '🂫': 11, '🂭': 12, '🂮': 13,
          '🂱': 14, '🂲': 2, '🂳': 3, '🂴': 4, '🂵': 5, '🂶': 6, '🂷': 7, '🂸': 8, '🂹': 9, '🂺': 10, '🂻': 11, '🂽': 12, '🂾': 13,
          '🃁': 14, '🃂': 2, '🃃': 3, '🃄': 4, '🃅': 5, '🃆': 6, '🃇': 7, '🃈': 8, '🃉': 9, '🃊': 10, '🃋': 11, '🃍': 12, '🃎': 13,
          '🃑': 14, '🃒': 2, '🃓': 3, '🃔': 4, '🃕': 5, '🃖': 6, '🃗': 7, '🃘': 8, '🃙': 9, '🃚': 10, '🃛': 11, '🃝': 12, '🃞': 13}




def main():
    game_over = False
    tie = False
    round_counter = 1
    print("hey") #todo instructions
    how_many_players, list_of_players = init_players()
    cards_per_hand, all_players_hand, hand_values = init_cards(how_many_players)
    player, player_value = init_shuffle(how_many_players, cards_per_hand, all_players_hand, hand_values)
    assign_cards(list_of_players, player, player_value)
    while not game_over:
        game_over, loser_final = round(list_of_players, round_counter, game_over)
    print(f'\n\n{list_of_players[1-loser_final].name} beat {list_of_players[loser_final].name} --> '
          f'⚔{list_of_players[1-loser_final].points}⚔ to ⚔{list_of_players[loser_final].points}⚔!')
    print(f'This took {list_of_players[1-loser_final].name} {round_counter} rounds!')
    # mil_ha_ma_counter = 0



def init_players(): # determines number of players + creates their instances
    try:
        how_many_players = int(input("How many players will be playing today?\n"))
    except:
        print("Please input an integer...")
        return init_players()
    if how_many_players != 2:
        print("Currently only a 2 player game is supported...")
        print("Later versions could include more!")
        print("In the meantime, please enter 2")
        return init_players()
    else:
        list_of_players = []
        player_1 = Players(input("What is Player 1's name? \n"), [], [], 0)
        list_of_players.append(player_1)
        player_2 = Players(input("What is Player 2's name? \n"), [], [], 2)
        list_of_players.append(player_2)
    return how_many_players, list_of_players


def init_cards(how_many_players):
    cards_per_hand = 52 // how_many_players
    all_players_hand = []
    hand_values = []
    for i in range(52):
        random_key = random.choice(list(cards.keys()))
        random_value = cards[random_key]
        all_players_hand.append(random_value)
        hand_values.append(values[random_value])
        del cards[random_key]
    return cards_per_hand, all_players_hand, hand_values


def init_shuffle(how_many_players, cards_per_hand, all_players_hand, hand_values):
    player = []  # holds cards in hand
    player_value = []  # holds card values in hidden hand
    c = cards_per_hand
    for b in range(how_many_players):
        player.append(all_players_hand[c*b:c*(b+1)])
        player_value.append(hand_values[c*b:c*(b+1)])
    return player, player_value


def assign_cards(list_of_players, player, player_value):
    for i in range(len(list_of_players)):
        Players.set_cards_and_values(list_of_players[i], player[i], player_value[i])
        print(list_of_players[i].name, list_of_players[i].cards, list_of_players[i].card_values)


def redistribution(winner, loser, num_of_redistributions):
    winner_cards = []  # cards to be added to winner
    loser_cards = []  # cards to be removed from loser
    winner_values = []  # values to be added to winner
    loser_values = []  # values to be removed from loser
    to_remove_cards_w = []  # cards to be removed from winner's beginning (will end up in the end)
    to_remove_values_w = []   # values to be removed from winner's beginning (will end up in the end)
    for card in range(num_of_redistributions):
        winner_cards.append(winner.cards[card])
        to_remove_cards_w.append(winner.cards[card])
        winner_values.append(winner.card_values[card])
        to_remove_values_w.append(winner.card_values[card])
        winner_cards.append(loser.cards[card])
        winner_values.append(loser.card_values[card])
        loser_cards.append(loser.cards[card])
        loser_values.append(loser.card_values[card])
    Players.update_cards_and_values(loser, loser_cards, loser_values, False)
    Players.update_cards_and_values(winner, to_remove_cards_w, to_remove_values_w, False)
    Players.update_cards_and_values(winner, winner_cards, winner_values, True)
    winner.points += num_of_redistributions  # todo unclear if this works...


def round(list_of_players, round_counter, game_over):
    for i in range(len(list_of_players)):
        if len(list_of_players[i].cards) == 0:
            return True, i  # todo alternatively, need to return game = false
    print(f'Round {round_counter}')
    card_battle = []
    for j in range(len(list_of_players)):
        print(f'{list_of_players[j].name} has: {list_of_players[j].cards[0]}')
        print(f'{list_of_players[j].cards}')
        print(f'{list_of_players[j].card_values}')
        card_battle.append(list_of_players[j].card_values[0])
    round_winner, num_of_milhama, less_hidden_cards = compare_cards(list_of_players, card_battle, 0, 0)
    if round_winner == None:
        print("That was crazy!")
        print("Let's continue...")
    else:
        redistribution(list_of_players[round_winner], list_of_players[1-round_winner], 1 + 3*num_of_milhama)
        # todo check if less_hidden_cards matters here (necessary or already taken care of)
        round_counter += 1
    return False, 0





def compare_cards(list_of_players, card_battle, num_of_milhamot, less_hidden_cards):
    if card_battle[0] > card_battle[1]:
        print(f'{list_of_players[0].name} wins!')
        return 0, num_of_milhamot, less_hidden_cards
    elif card_battle[0] < card_battle[1]:
        print(f'{list_of_players[1].name} wins!')
        return 1, num_of_milhamot, less_hidden_cards
    return mil_ha_ma(list_of_players, card_battle, num_of_milhamot+1, less_hidden_cards)


def mil_ha_ma(list_of_players, card_battle, num_of_milhamot, less_hidden_cards):
    problematic_player = 0
    cards_to_hide = 3*num_of_milhamot
    for i in range(len(list_of_players)):
        if len(list_of_players[i].cards) < 3*num_of_milhamot:
            cards_to_hide = len(list_of_players[i].cards) % 3 + 3*(num_of_milhamot-1)
            problematic_player = i
    if cards_to_hide == 3*num_of_milhamot:
        print("Mil")
        print(''.join(str((list_of_players[j].name + ":" + list_of_players[j].cards[cards_to_hide-2] + " ")) for j in
                      range(len(list_of_players))))
        print("Ha")
        print(''.join(str((list_of_players[j].name + ":" + list_of_players[j].cards[cards_to_hide - 1] + " ")) for j in
                      range(len(list_of_players))))
        print("MA!")
        print(''.join(str((list_of_players[j].name + " has " + list_of_players[j].cards[cards_to_hide] + "\n")) for j in
                      range(len(list_of_players))))
        next_card_battle = [list_of_players[k].card_values[cards_to_hide] for k in range(len(list_of_players))]
        return compare_cards(list_of_players, next_card_battle, num_of_milhamot + 1)
    else:
        less_hidden_cards = cards_to_hide % 3 # number of cards left to open in total
        if less_hidden_cards == 0:
            return tie_on_last_card(list_of_players, num_of_milhamot, problematic_player)
        print(f"{list_of_players[problematic_player].name} doesn't have enough cards to complete the Milhama!")
        print("This means that this is potentially the final round of the match!")
        print("Mil")
        print("Ha")
        print("MA!")
        for l in range(less_hidden_cards-1):
            print(''.join(
                str("("+(list_of_players[j].name + ":" + list_of_players[j].cards[cards_to_hide + l] + ") ")) for j in
                range(len(list_of_players))))
        card_battle_pl = []
        for m in range(len(list_of_players)):
            print(f'{list_of_players[m].name} has: {list_of_players[m].cards[less_hidden_cards-1]}')
            card_battle_pl.append(list_of_players[m].card_values[less_hidden_cards-1])
        if card_battle_pl[0] == card_battle_pl[1]:
            return tie_on_last_card(list_of_players, num_of_milhamot, problematic_player)
        return compare_cards(list_of_players, card_battle_pl, num_of_milhamot, less_hidden_cards)

def tie_on_last_card(list_of_players, num_of_milhamot, problematic_player):
    print(f'The result of this round is a tie, and {list_of_players[problematic_player].name} has no more'
          f' cards left!')
    print("Therefore, we will continue the game by returning the cards in question back to their"
          " respective players...")
    cards_to_return = len(list_of_players[problematic_player].cards)
    for i in range(len(list_of_players)):
        Players.update_cards_and_values(list_of_players[i], list_of_players[i].cards[0:cards_to_return],
                                        list_of_players[i].card_values[0:cards_to_return], True)
        Players.update_cards_and_values(list_of_players[i], list_of_players[i].cards[0:cards_to_return],
                                        list_of_players[i].card_values[0:cards_to_return], False)
    return None, None, 0



main()
