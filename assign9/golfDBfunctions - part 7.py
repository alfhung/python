# import sqlite3 module
import sqlite3

# get player name from user
# display player scores or error if player not in table
def queryDB(cursor):
    keep_entering = 'y'
    while keep_entering == 'y':
        entry = input('Please enter the name of a player: ')
        cursor.execute('select * from players where name = ?', (entry,))
        player = cursor.fetchone()
        # determine if player name in table
        if player == None:
            print('Error!!')
        else:
            avg_gross = player[2]/player[3]
            tot_pars = int(player[4])
            tot_bird = int(player[5])
            tot_handicap = hand_point(avg_gross)
            print('For %s:\n'\
                  'Average Gross Score is %.2f,\n'\
                  'Total number of Pars is %d,\n'
                  'Total number of Birdies is %d,\n'\
                  'Corresponding Handicap is %d.'
                   %(entry,avg_gross,tot_pars,tot_bird,tot_handicap))
        # prompt for user if want to input more names
        keep_entering = input('Do you want to enter more names? '\
                              'Enter y (yes) or press enter to finish: ')

# find handicap points based on average gross score
def hand_point(avg_gross):
    avg_score = int(avg_gross)
    # create average score list
    set_avg_score = list(range(38,60))
    # create handicap points list
    set_handicap = [1,2,2,3,4,5,6,6,7,8,9,10,10,\
                    11,11,12,13,14,15,16,17,17]
    # find corresponding handicap points
    if avg_score < 38:
        handy_point = 0
    elif avg_score > 59:
        handy_point = 18
    else:
        # set accumulator to use as index
        value = 0
        # get value of index from average gross list
        if avg_score in set_avg_score:
            new_list = list(range(38,avg_score+1))
            for i in new_list:
                value = value + 1
        # modify to correct value of index
        index_num = value - 1
        handy_point = set_handicap[index_num]
    return handy_point
        
# set up connection with database and close it when finish
def main():
    conn = sqlite3.connect('C:/Users/alfhung/Desktop/assignment 9/golf')
    cursor = conn.cursor()
    queryDB(cursor)
    cursor.close()

# call main function    
main()
