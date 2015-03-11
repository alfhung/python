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
            print('For %s:\n'\
                  'Average Gross Score is %.2f,\n'\
                  'Total number of Pars is %d,\n'
                  'Total number of Birdies is %d.'\
                   %(entry,avg_gross,tot_pars,tot_bird))
        # prompt for user if want to input more names
        keep_entering = input('Do you want to enter more names? '\
                              'Enter y (yes) or press enter to finish: ')
        
# set up connection with database and close it when finish
def main():
    conn = sqlite3.connect('C:/Users/alfhung/Desktop/assignment 9/golf')
    cursor = conn.cursor()
    queryDB(cursor)
    cursor.close()

# call main function    
main()
