# ------------------------------------------------------------------------------
# BLACKJACK GAME
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# In-Class Project4 – V.1.0
# ______________________________________________________________________________

#
# -- Imported Modules

import random


#
# -- Card Class
class Card(object):

    #
    # -- NOTE!: Moved the ranks list to this class. Permission by Prof. Bauer
    suits = ['♠', '♥', '♦', '♣']

    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}

    #
    # -- Card Constructor Method
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    #
    # -- Card Value Method
    def value(self, total):

        soft_ace = 11  # -- An Ace valued at 11

        soft_limit = 21  # -- Max score for an Ace to be valued at 11

        #
        # -- Computes card values. Values for Aces depend on current score
        if self.rank != 'A':
            return Card.values[self.rank]

        elif total + soft_ace <= soft_limit:
            return soft_ace

        else:
            return Card.values[self.rank]

    #
    # -- String Method
    def __str__(self):
        return '|{} of {}|'.format(self.rank, self.suit)


#
# -- Make Deck Function
def make_deck():

    #    NOTE!
    # -- Moved the ranks list to the Card class. Permission by Prof. Bauer

    deck = []  # -- Will hold the deck of cards

    for suit in Card.suits:  # -- Builds and stores required cards
        for rank in Card.ranks:
            deck.append(Card(suit, rank))

    random.shuffle(deck)
    return deck


#
# -- Main Function
def main():

    deck = make_deck()

    player_score = 0
    player_hand = []

    player_turn = True
    first_draw = True

    print("\nWELCOME TO OSKY'S BLACKJACK PALACE")

    #
    # -- Runs the player's turn in the game
    while player_turn and player_score < 21:

        if first_draw:

            card = deck.pop(0)
            card_value = card.value(player_score)
            player_score += card_value
            player_hand.append(card)
            first_draw = False
            print('\nYour first card is:', card)

        else:

            choice = input('\nDo you want another card? Type (y/n): ')

            if choice.lower() == 'y':

                card = deck.pop(0)
                card_value = card.value(player_score)
                player_score += card_value
                player_hand.append(card)

                print('\nYour hand: ', *player_hand)

            elif choice.lower() == 'n':

                player_turn = False

    #
    # -- Evaluates the status of the game | Halts if player wins
    continue_game = True

    if player_score == 21:

        print('\nBlackjack! You Win! ヽ(^o^)丿\n')
        continue_game = False

    elif player_score > 21:

        print('\nBust! You lose! (~_~メ)\n')
        continue_game = False

    #
    # -- Runs the Dealer's turn in the game
    if continue_game:

        dealer_score = 0
        dealer_hand = []
        print("\n>>>> Dealer's Turn <<<<\n")

        while dealer_score <= 17:
            card = deck.pop(0)
            card_value = card.value(dealer_score)
            dealer_score += card_value
            dealer_hand.append(card)

        print("Dealer's hand: ", *dealer_hand)

        if dealer_score == 21:

            print("\nDealer's Blackjack! You lose! (*￣m￣)\n")

        elif dealer_score > 21:

            print("\nDealer bust! You win! ヽ(^。^)ノ\n")

        elif dealer_score > player_score:

            print("\nDealer's high! You lose! （ ﾟ Дﾟ)\n")

        elif dealer_score < player_score:

            print("\nPlayer's high! You win! (＾▽＾)\n")

        else:

            print("\nMatching scores. It's a tie! ¯\\_(ツ)_/¯\n")


if __name__ == '__main__':
    main()









