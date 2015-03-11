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


