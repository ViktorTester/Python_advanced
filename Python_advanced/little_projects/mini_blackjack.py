"""Rules of the game
The player scores points by rolling the 11-sided die multiple times
with the goal of getting as close to 21 points as possible.

If a player scores exactly 21 points, he automatically wins the game.

If the player has more than 21 points, he "went over" and the dealer
wins the game. The player chooses when he wants to stop the die roll.

If the player has not "overdrawn", the dealer begins to roll the die.
As long as the dealer has 16 points or fewer, he will roll the die to score
points. If the dealer has 17 points or more, he will stop rolling the die.

If the dealer has more than 21 points, he "went through" and the player wins the game.

If neither the player nor the dealer has "overdrawn", the one
with the most points wins. If there is a tie, the dealer wins."""

import random
import sys

print("""--------------------
Welcome to BlackJack
--------------------""")

print("""The dealer rolls
while he has < 17
--------------------""")


def game(player_score):
    """Player's part"""
    print(f'Player score = {player_score}')
    print("""hit  | roll the dice
hold | stop""")
    next_step = input(f'{player_score} > ')
    print('--------------------')
    return next_step


def dealer_game(player_score):
    """Dealer's part"""
    print(f'Player score = {player_score}')
    dealer_score = 0
    while dealer_score < 17:
        dealer_score += random.randint(1, 12)
        print(f'Dealer score = {dealer_score}')
    if dealer_score > 21:
        print('You won!')
        sys.exit()
    return dealer_score


player_score = 0

next_step = game(player_score)

while next_step == 'hit':
    if player_score == 21:
        print('You won!')
        break
    if player_score > 21:
        print('You lose!')
        break
    player_score += random.randrange(1, 12)
    next_step = game(player_score)
else:
    dealer_score = dealer_game(player_score)

    if player_score > dealer_score:
        print('You won!')
    else:
        print('You lose!')