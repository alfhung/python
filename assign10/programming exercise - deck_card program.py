# create a deck object
# deal out 2 hands, each of 5 cards
# display cards in each hand
# display number cards in deck after dealing cards
# return all cards objects to deck
# display number cards in deck after returning all cards

import random
import cards

# use drawRandom method to deal cards
def dealing(deck):
    # initialize lists for cards
    hand1 = []
    hand2 = []
    
    for num1 in range(5):
        card1 = deck.drawRandom()
        card_obj1 = str(card1)
        hand1.append(card_obj1)
        
    for num2 in range(5):
        card2 = deck.drawRandom()
        card_obj2 = str(card2)
        hand2.append(card_obj2)

    return hand1,hand2,deck

# display cards in each hand
def show_cards(hand1,hand2):
    print('The cards in hand 1 are:')
    for num in hand1:
        print(num)
    print('The cards in hand 2 are:')
    for value in hand2:
        print(value)

# display number cards currently in deck
def num_card1(new_deck):
    numCards1 = new_deck.getNumCards()
    print('The current number of cards after dealing is',numCards1)

# return all card objects to deck
def return_cards(hand1,hand2,new_deck):
    for card1 in hand1:
        new_deck.returnCardtoDeck(card1)
    for card2 in hand2:
        new_deck.returnCardtoDeck(card2)
    return hand1,hand2,new_deck

# display number cards after returning all cards
def num_card2(getCards):
    reset_deck = getCards.getNumCards()
    print('The number of cards after returning all cards is'\
          , reset_deck)

def main():
    # create deck object
    deck = cards.Deck()

    # deal cards, get two hands and new deck
    hand1,hand2,new_deck = dealing(deck)

    # display cards in each hand
    hands = show_cards(hand1,hand2)

    # display number cards currently in deck
    deck_num1 = num_card1(new_deck)

    # return all card objects to deck
    new_hand1,new_hand2,getCards = return_cards(hand1,hand2,new_deck)

    # display number cards after returning all cards
    deck_num2 = num_card2(getCards)

# call main function
main()
