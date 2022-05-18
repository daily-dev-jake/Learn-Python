# Create a Card class
# should understand suit, rank, value of card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    '''Individual Card with types: Suit, Rank, Value'''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    def __init__(self):
        # init 52 cards
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
        
#TODO Player class!

new_deck = Deck()
new_deck.shuffle()
for i in range(5):
    print(new_deck.all_cards[i])    

"""three_clubs = Card("Clubs","Three")
print(three_clubs)"""