'''
How is the game played ?
https://www.pagat.com/banking/blackjack.html
'''

import random

class Blackjack():
    deck = {"A":1,"J":10,"Q":10,"K":10,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
    cards_opened = []



    def autowin(self,cards):
        '''
        The best possible blackjack hand is an opening deal of an ace with any ten-point card.
        This is called a "blackjack", or a natural 21, and the player holding this automatically
        wins unless the dealer also has a blackjack
        :return:
        '''
        pass

    def opencard(self):
        '''
        return a random card picked up from the deck
        Continue picking up a card if the card was previously opened
        :return:
        '''
        while True:
            card = random.choice(self.deck.keys())
            if card in self.cards_opened:
                continue
            else:
                self.cards_opened.append(card)
                return card

class Player():
    bet = 0
    winnings = 0
    losses = 0
    current_card = None
    opened_cards = []

class Dealer():
    cards = []
    hole_card = None





player = Player()
player.bet =
dealer = Dealer()
Blackjack().opencard()