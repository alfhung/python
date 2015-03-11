# call function and enter number players as parameter
# create list of n players
# n players play againg n-1 players in n-1 rounds
# display n-1 rounds

def scheduling(total_players):
    games_round = len(total_players)//2
    # choose 1 player
    player1 = total_players.pop(0)
    # number of rounds
    for number in total_players:
        print('Round',number-1)
        game = 0
        check = 0
        # who play who
        for value in total_players:
            game = game + 1
            check = check - 1
            print('Player',total_players[game-1],'vs Player', total_players[check+1])
            
def tournament(number_players):
    total_players = list(range(1,number_players + 1))

    schedule = scheduling(total_players)
