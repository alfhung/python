Assignment 10

Part 1:
Programming Exercise 2:
Code:
# define class definition for a car
class Car:
    # define constructor
    def __init__(self,year_model,make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # define accesor methods
    def get_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    # define mutator methods
    def accelerate(self):
        self.__speed = self.__speed + 5
        return self.__speed

    def brake(self):
        self.__speed = self.__speed - 5
        return self.__speed

    # method returns current speed
    def get_speed(self):
        return self.__speed

# program create car object
# calls accelerate method 5 times
# return current speed after each call to accelerate
# then calls brake method 5 times
# return current speed after each call to brake

def car(year_model,make):
    # create object from car
    car_obj = Car(year_model,make)

    # call function to display car model and made
    model = car_model(car_obj)

    # call functions to display speed after accelerating
    # and braking 5 times
    speed_accelerate = accelerating(car_obj)
    speed_brake = braking(car_obj)
    
# display the model of the car
def car_model(car_obj):
    print('The model of your car is %d' % (car_obj.get_model()))
    print('Your car is made of ' + car_obj.get_make())

# call accelerate method 5 times, then display speed
def accelerating(car_obj):
    for num in range(5):
        speed = car_obj.accelerate()

    print('The current speed is ',speed)

# call brake method 5 times, then display speed
def braking(car_obj):
    for value in range(5):
        speed = car_obj.brake()

    print('The current speed is ',speed)

Test Case:
>>> car(1980,'metal')
The model of your car is 1980
Your car is made of metal
The current speed is  25
The current speed is  0

Part 3:
Card and Deck Class Program:
Code:
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

Test Cases:
The cards in hand 1 are:
5 of Clubs
9 of Hearts
10 of Clubs
Jack of Clubs
5 of Diamond
The cards in hand 2 are:
2 of Clubs
3 of Spades
8 of Diamond
2 of Diamond
6 of Spades
The current number of cards after dealing is 42
The number of cards after returning all cards is 52

The cards in hand 1 are:
9 of Diamond
3 of Clubs
5 of Diamond
5 of Clubs
8 of Spades
The cards in hand 2 are:
Jack of Clubs
3 of Diamond
6 of Spades
2 of Spades
5 of Spades
The current number of cards after dealing is 42
The number of cards after returning all cards is 52

The cards in hand 1 are:
9 of Hearts
Ace of Hearts
Jack of Clubs
5 of Spades
10 of Clubs
The cards in hand 2 are:
6 of Hearts
5 of Clubs
6 of Clubs
Ace of Clubs
7 of Spades
The current number of cards after dealing is 42
The number of cards after returning all cards is 52

