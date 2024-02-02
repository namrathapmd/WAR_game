# WAR CARD GAME!
# The objective of the game is to win all of the cards.

# The deck is divided evenly among the players, giving each a down stack. In unison, each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack.
# If the two cards played are of equal value, then there is a "war". Both players place the next card from their pile face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.


# CARD
# SUIT, RANK, VALUE

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit, rank)

                # fill up the all_cards list with all card objects
                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)  # doesn't return anything

    def deal_one(self):

        return self.all_cards.pop()

# Let's create a Player Class, a player should be able to hold instances of Cards, they should also be able to remove and add them from their hand. We want the Player class to be flexible enough to add one card, or many cards so we'll use a simple if check to keep it all in the same method.


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    # top card is removed
    def remove_one(self):
        return self.all_cards.pop(0)

    # add cards to bottom
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# GAME LOGIC
# -----------------------------------------------------------------------
# create player 1 and player 2

# create a deck

# shuffle the deck

# split half and add half to player 1 and other half to player 2

# check for every round if any one has lost (any player has 0 cards)

# game_on is true until the above condition

# each player removes a card (from top obvio) and we do a comparison

# whichever wins that (either player 1 > player 2 ---OR--- player 1 < player 2), both cards get added to their deck

# WAR!! (player 1 == player 2) at_war = True

# While at_war loop: why while loop? coz you can get two wars in a row

# -----------------------------------------------------------------------
# GAME SETUP

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
at_war = True

round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    # check to see if a player is out of cards
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!!')
        game_on = False
        break

    # Otherwis, the game is still ON!

    # START A NEW ROUND and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # COMPARISON
    at_war = True

    while at_war:
        # if player 1 has upper value card, add all cards to player 1
        if player_one_cards[-1].value > player_two_cards[-1].value:
            print(
                f'Player 1: {player_one_cards[-1].suit},{player_one_cards[-1].rank},{player_one_cards[-1].value}')
            print(
                f'Player 2: {player_two_cards[-1].suit},{player_two_cards[-1].rank},{player_two_cards[-1].value}')
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        # if player 2 has lower value card, add all cards to player 2
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            print(
                f'Player 1: {player_one_cards[-1].suit},{player_one_cards[-1].rank},{player_one_cards[-1].value}')
            print(
                f'Player 2: {player_two_cards[-1].suit},{player_two_cards[-1].rank},{player_two_cards[-1].value}')
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        # if both are equal value: WAR!!
        # we will grab another card each and continue the war
        elif player_two_cards[-1].value == player_one_cards[-1].value:
            print(
                f'Player 1: {player_one_cards[-1].suit},{player_one_cards[-1].rank},{player_one_cards[-1].value}')
            print(
                f'Player 2: {player_two_cards[-1].suit},{player_two_cards[-1].rank},{player_two_cards[-1].value}')

            print('WAR!')

            # we need to check if player has enough cards to play
            # here, we check if players have min 5 cards to continue playing war
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war!")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war!")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            # otherwise we are still at war, so we will add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
