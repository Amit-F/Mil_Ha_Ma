# to-do:
# 1. fix "1 points" bug
# 2. find a way to make the game end when 1 player reaches 0 cards
# 3. make code more efficient (loop all appends + removes)
    # a. use list comprehensions!
# 4. for multiplayer, make for loop that adds empty lists to master list and work on indices

import random

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

player_1_name = input("What is Player 1's name? \n")
player_2_name = input("What is Player 2's name? \n")

cards_per_hand = 52 // 2

player = []  # holds cards in hand
player_value = []  # holds card values in hidden hand

all_players_hand = []
hand_values = []
