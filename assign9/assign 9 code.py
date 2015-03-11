Assignment 9

Programming Exercise
Part 1:
Code:
import sqlite3

# file contains functions used to create, view and update 
# data stored about the players in a golf league

# obtain and return a connection object and a cursor object 
# which can be used to access the database named golf
def getgolfdatabasecursor():
    connection = sqlite3.connect('golf')
    cursor = connection.cursor()
    return connection, cursor    

# create a table named players as part of the database named golf
# each row of the table represents a player.  The data fields for each
# player are:  number, name, total gross score, total rounds played,
# number of pars and number of birdies.
def createPlayerTable():
    connection, cursor = getgolfdatabasecursor()
    cursor.execute('drop table if exists players ') 
    cursor.execute('''create table players(
                         playernum integer,
                         name text,
                         totalGross integer,
                         totalRounds integer,
                         pars integer,
                         birdies integer)'''
                   )
    
    # add record to the table for each player whose name is in the file players.txt
    fileName = 'players.txt'
    datafile = open(fileName, 'r')
    playerNum = 1
    for aline in datafile:
        playerName = aline.strip()
        playerData = (playerNum, playerName, 0, 0, 0, 0)
        cursor.execute('''insert into players(
                            playernum, name, totalGross, totalRounds, 
                            pars, birdies) 
                            values(?,?,?,?,?,?)''', playerData
                       )
        playerNum += 1
        
    connection.commit() # needed in order for changes to take effect
    connection.close()
    datafile.close()
    print('Player Table created with %d rows.' % (playerNum-1))

# display all of the data stored in the table players
def viewPlayerTable():
    connection, cursor = getgolfdatabasecursor()
    cursor.execute('''select * from players order by name''')
    result = cursor.fetchall()
    print('Name      totalGross  totalRound  pars  birdies')
    for row in result:
        print('%-12s     %d        %d         %d        %d' % \
              (row[1], row[2], row[3], row[4], row[5]))
    connection.close()


# update database with scores read from a file    
def enterScores():
    connection, cursor = getgolfdatabasecursor()
    scoresFileName = input('Enter name of file containing scores:  ')
    scoresFile = open(scoresFileName, 'r')
    for line in scoresFile:
        data = line.split()
        name = data[0]
        scores = data[1:]
        gross = 0
        for i in range(len(scores)):
            scores[i] = int(scores[i])       
            gross += scores[i]
        # for HW9 you will write a function that is passed scores and
        # returns the number of pars and the number of birdies
        cursor.execute('''update players set totalgross = totalgross + ?,
                                             totalrounds = totalrounds + 1
                           where name = ?''' ,(gross, name)
                       )
    scoresFile.close()
    connection.commit()
    connection.close()
    print('data base updated')

# define a function that will compute and return the number of pars
# and the number of birdies here.

Test Cases:
createPlayerTable()
Player Table created with 8 rows.
viewPlayerTable()
Name      totalGross  totalRound  pars  birdies
Betty            0        0         0        0
Elena            0        0         0        0
Ezgi             0        0         0        0
Jane             0        0         0        0
Margaret         0        0         0        0
Ricki            0        0         0        0
Rosalia          0        0         0        0
Ruth             0        0         0        0

Part 2-4:
Code:
import sqlite3

# file contains functions used to create, view and update 
# data stored about the players in a golf league

# obtain and return a connection object and a cursor object 
# which can be used to access the database named golf
def getgolfdatabasecursor():
    connection = sqlite3.connect('golf')
    cursor = connection.cursor()
    return connection, cursor    

# create a table named players as part of the database named golf
# each row of the table represents a player.  The data fields for each
# player are:  number, name, total gross score, total rounds played,
# number of pars and number of birdies.
def createPlayerTable():
    connection, cursor = getgolfdatabasecursor()
    cursor.execute('drop table if exists players ') 
    cursor.execute('''create table players(
                         playernum integer,
                         name text,
                         totalGross integer,
                         totalRounds integer,
                         pars integer,
                         birdies integer)'''
                   )
    
    # add record to the table for each player whose name is in the file players.txt
    fileName = 'players.txt'
    datafile = open(fileName, 'r')
    playerNum = 1
    for aline in datafile:
        playerName = aline.strip()
        playerData = (playerNum, playerName, 0, 0, 0, 0)
        cursor.execute('''insert into players(
                            playernum, name, totalGross, totalRounds, 
                            pars, birdies) 
                            values(?,?,?,?,?,?)''', playerData
                       )
        playerNum += 1
        
    connection.commit() # needed in order for changes to take effect
    connection.close()
    datafile.close()
    print('Player Table created with %d rows.' % (playerNum-1))

# display all of the data stored in the table players
def viewPlayerTable():
    connection, cursor = getgolfdatabasecursor()
    cursor.execute('''select * from players order by name''')
    result = cursor.fetchall()
    print('Name      totalGross  totalRound  pars  birdies')
    for row in result:
        print('%-12s     %d        %d         %d        %d' % \
              (row[1], row[2], row[3], row[4], row[5]))
    connection.close()

# update database with scores read from a file    
def enterScores():
    connection, cursor = getgolfdatabasecursor()
    # get name of file and read file
    scoresFileName = input('Enter name of file containing scores:  ')
    scoresFile = open(scoresFileName, 'r')
    for line in scoresFile:
        # separate elements into a list
        data = line.split()
        # index into list to obtain name and scores
        name = data[0]
        scores = data[1:]
        # set accumulators
        gross = 0
        rounds = 0
        pars = 0
        birdies = 0
        set_par = [4,3,4,3,4,5,4,3,5]
        for i in range(len(scores)):
            scores[i] = int(scores[i])
            gross += scores[i]
            # call function to get pars and birdies
            pars, birdies = num_par_bird(i,set_par,scores,rounds,pars,birdies)
            rounds += 1
        # for HW9 you will write a function that is passed scores and
        # returns the number of pars and the number of birdies
        cursor.execute('''update players set totalgross = totalgross + ?,
                                             totalrounds = totalrounds + 1,
                                             pars = pars + ?,
                                             birdies = birdies + ?
                           where name = ?''' ,(gross,pars,birdies,name)
                       )
    scoresFile.close()
    connection.commit()
    connection.close()
    print('data base updated')

# define a function that will compute and return the number of pars
# and the number of birdies here.
def num_par_bird(i,set_par,scores,rounds,pars,birdies):
    scores[i] = int(scores[i])
    if scores[i] == set_par[rounds]:
        pars = pars + 1
    elif scores[i] < set_par[rounds]:
        birdies = birdies  + 1
    return pars,birdies

Test Cases:
>>> enterScores()
Enter name of file containing scores:  week1scores.txt
data base updated
>>> viewPlayerTable()
Name      totalGross  totalRound  pars  birdies
Betty            49        1         2        1
Elena            50        1         1        1
Ezgi             45        1         2        1
Jane             43        1         1        2
Margaret         46        1         1        2
Ricki            46        1         1        1
Rosalia          52        1         1        0
Ruth             40        1         1        4
>>> enterScores()
Enter name of file containing scores:  week2scores.txt
data base updated
>>> viewPlayerTable()
Name      totalGross  totalRound  pars  birdies
Betty            93        2         4        2
Elena            98        2         3        1
Ezgi             90        2         4        2
Jane             84        2         2        4
Margaret         84        2         4        4
Ricki            93        2         2        1
Rosalia          97        2         3        0
Ruth             81        2         3        6

Part 5:
Code:
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

Test Cases:
Please enter the name of a player: Ruth
For Ruth:
Average Gross Score is 40.50,
Total number of Pars is 3,
Total number of Birdies is 6.
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Margaret
For Margaret:
Average Gross Score is 42.00,
Total number of Pars is 4,
Total number of Birdies is 4.
Do you want to enter more names? Enter y (yes) or press enter to finish: 
>>> 
Please enter the name of a player: Sean
Error!!
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Jane
For Jane:
Average Gross Score is 42.00,
Total number of Pars is 2,
Total number of Birdies is 4.
Do you want to enter more names? Enter y (yes) or press enter to finish: 
Please enter the name of a player: Ezgi
For Ezgi:
Average Gross Score is 45.00,
Total number of Pars is 4,
Total number of Birdies is 2.
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Alf
Error!!
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: 24Jo
Error!!
Do you want to enter more names? Enter y (yes) or press enter to finish: 

Part 6:
Code:
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
    print('The corresponding handicap point of %d ' \
          'is %d' %(avg_score,handy_point))

Test Cases:
>>> hand_point(75)
The corresponding handicap point of 75 is 18
>>> hand_point(20)
The corresponding handicap point of 20 is 0
>>> hand_point(55)
The corresponding handicap point of 55 is 14

Part 7:
Code:
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

Test Cases:
Please enter the name of a player: Margaret
For Margaret:
Average Gross Score is 42.00,
Total number of Pars is 4,
Total number of Birdies is 4,
Corresponding Handicap is 4.
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Elena
For Elena:
Average Gross Score is 49.00,
Total number of Pars is 3,
Total number of Birdies is 1,
Corresponding Handicap is 10.
Do you want to enter more names? Enter y (yes) or press enter to finish: 
>>> 
Please enter the name of a player: Yoyo
Error!!
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Betty
For Betty:
Average Gross Score is 46.50,
Total number of Pars is 4,
Total number of Birdies is 2,
Corresponding Handicap is 7.
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Jane
For Jane:
Average Gross Score is 42.00,
Total number of Pars is 2,
Total number of Birdies is 4,
Corresponding Handicap is 4.
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Ish
Error!!
Do you want to enter more names? Enter y (yes) or press enter to finish: 
>>> 
Please enter the name of a player: 24
Error!!
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Ruth
For Ruth:
Average Gross Score is 40.50,
Total number of Pars is 3,
Total number of Birdies is 6,
Corresponding Handicap is 2.
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Max
Error!!
Do you want to enter more names? Enter y (yes) or press enter to finish: y
Please enter the name of a player: Rosalia
For Rosalia:
Average Gross Score is 48.50,
Total number of Pars is 3,
Total number of Birdies is 0,
Corresponding Handicap is 9.
Do you want to enter more names? Enter y (yes) or press enter to finish: 
>>> 
