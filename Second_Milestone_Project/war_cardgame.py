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
class Player:
    '''1. Player should be able to add both 'a single card' or 'multiple cards' to their list on hand.
    2. Player class should allow translating a Deck (hand of cards) with a bottom / top from the stack of a Python List. (Draw card = Deck -1 from top & Hand +1 on top) 
    3. Player play a card (top card of hand will be played) = cards.pop(0)
    4. Player add to end of list = cards.append('card1')
    5. If adding multiple cards to Player hand (to merge 1 list to another), = cards.extend([card1,card2])
    '''
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        '''Removes first card'''
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        ''' Uses diff methods to add cards into player's hand properly'''
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

new_deck = Deck()
new_deck.shuffle()

player1 = Player("Jose")
print(player1)
player1card = new_deck.deal_one()

player1.add_cards(player1card)
print(player1card)
print(player1)

"""three_clubs = Card("Clubs","Three")
print(three_clubs)"""