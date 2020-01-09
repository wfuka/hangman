# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:28:28 2020

@author: hukam
"""

from random import shuffle
import Card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card.Card(i, j))
        shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


#deck = Deck()
#for card in deck.cards:
#    print(card)
