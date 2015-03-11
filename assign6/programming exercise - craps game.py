# call to play 100 games of craps
# decide if won or lost game based on outcome of dice
# display number of wins and lost
# display percent won after 100 games

# import functions from random module
import random

# determine number of games won and lost after rolling dice
def rolling():
    # set accumulators
    win = 0
    lost = 0

    # loop iterates for 100 games
    for dice in range (0,100):
        # obtain value after rolling dice
        value = random.randrange(2,13)

        # determine if player won or lost based on outcome
        if value == 7 or value == 11:
            win = win + 1
        elif value == 2 or value == 3 or value == 12:
            lost = lost + 1
        else:
            # save initial roll point
            initial_point = value

            # initialize condition
            check = True
            
            # reroll dice until get a 7 or initial point value
            while check == True:
                value = random.randrange(2,13)
            
                if value == initial_point:
                    win = win + 1
                    check = False
                elif value == 7:
                    lost = lost + 1
                    check = False

    # call percent function
    percentage = percent(win,lost)
    return percentage

# display number games won and lost and calculate percent won
def percent(win,lost):
    print('Number of wins is',win,'Number of lost is', lost)
    percent = win/100
    return percent

# call roll function and print percent games won
def main():
    # note: I have tried to place the for loop in the main function
    # before calling the function roll, however by doing that the results
    # display 0 for both the percent and the number of wins
    roll = rolling()
    print('Your percent games won after 100 games is',roll)

# call main function
main()
