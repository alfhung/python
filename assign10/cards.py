# class definitions for card and deck
import random

# define Card class
class Card:
    # define the data attributes for constructor
    def __init__(self,rank,suit):
        self.__rank = rank
        self.__suit = suit

    # define accesor methods for data attributes
    def getRank(self):
        return self.__rank

    def getSuit(self):
        return self.__suit

    def BJValue(self):
        if self.__rank == 11 or self.__rank == 12 or self.__rank == 13:
            return 10
        else:
            return self.__rank

    # modify __str__ to display rank and suit of card
    def __str__(self):
        ranks = ['','Ace','2','3','4','5','6','7',\
                 '8','9','10','Jack','Queen','King']        
        if self.__suit == 'd':
            suit = 'Diamond'
        elif self.__suit == 'h':
            suit = 'Hearts'
        elif self.__suit == 's':
            suit = 'Spades'
        elif self.__suit == 'c':
            suit = 'Clubs'
        return ranks[self.__rank] + ' of ' + suit

class Deck:
    # define constructor
    def __init__(self):
        self.__deck = []
        # create diamonds
        for diamonds in range(1,14):
            suit = 'd'
            card = Card(diamonds,suit)
            self.__deck.append(card)
        # create hearts
        for hearts in range(1,14):
            suit = 'h'
            card = Card(hearts,suit)
            self.__deck.append(card)
        # create spades 
        for spades in range(1,14):
            suit = 's'
            card = Card(spades,suit)
            self.__deck.append(card)
        # create clubs   
        for clubs in range(1,14):
            suit = 'c'
            card = Card(clubs,suit)
            self.__deck.append(card)
            
    # get number of cards in deck
    def getNumCards(self):
        return len(self.__deck)

    # remove card from top
    def drawTop(self):
        top = self.__deck[0]
        self.__deck.remove(top)
        return top

    # remove card from deck
    def drawRandom(self):
        card = random.choice(self.__deck)
        self.__deck.remove(card)
        return card

    # place removed card to bottom of deck
    def returnCardtoDeck(self,card):
        self.__deck.append(card)
