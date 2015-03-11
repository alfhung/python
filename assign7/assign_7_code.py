Assignment 7

Part I: Algorithm Workbench
Chapter 7 - Algorithm Workbench
1)
show = open('my_name.txt','w')
show.write('Alfredo Hung\n')
show.close()

2)
show = open('my_name.txt','r')
name = show.read()
show.close()
print(name)

3)
def main():
    file = open('number_list.txt','w')
    for line in range(0,101):
        file.write(str(line)+'\n')
    file.close()

4)
def main():
    file = open('number_list.txt','r')
    add = 0
    for line in file:
        value = line.rstrip('\n')
        add = add + int(value)

    print('The sum of the number is,',add)
    file.close()

Part II: Programming Exercises
Chapter 7 - Programming Exercise
3)
Code:
# ask user for file name
# 
# display file content

def content(file):
    file_opened = True
    while file_opened:
        try:
            in_file = open(file, 'r')
            file_opened = False
        except IOError:
            file = input('No such file in directory,'\
                         'Please enter another file name: ')
    return in_file

def read_file(in_file):
    new_file = open('new_file.txt','w')
    line = in_file.readline()
    line_num = 0
    while line != '':
        line = line.strip('\n')
        line_num = line_num + 1
        print('%d: ' %(line_num),line)
        line = in_file.readline()

        new_file.write(str(line_num) + str(line))
    
    new_file.close()

def main():
    file = input('Please enter a file name: ')
    in_file = content(file)
    add_number = read_file(in_file)
    
    in_file.close()

# call main function
main()

Test Cases:
Please enter a file name: programming exercise - craps game.py
1:  # call to play 100 games of craps
2:  # decide if won or lost game based on outcome of dice
3:  # display number of wins and lost
4:  # display percent won after 100 games
5:  
6:  # import functions from random module
7:  import random
8:  
9:  # determine number of games won and lost after rolling dice
10:  def rolling():
11:      # set accumulators
12:      win = 0
13:      lost = 0
14:  
15:      # loop iterates for 100 games
16:      for dice in range (0,100):
17:          # obtain value after rolling dice
18:          value = random.randrange(2,13)
19:  
20:          # determine if player won or lost based on outcome
21:          if value == 7 or value == 11:
22:              win = win + 1
23:          elif value == 2 or value == 3 or value == 12:
24:              lost = lost + 1
25:          else:
26:              # save initial roll point
27:              initial_point = value
28:  
29:              # initialize condition
30:              check = True
31:              
32:              # reroll dice until get a 7 or initial point value
33:              while check == True:
34:                  value = random.randrange(2,13)
35:              
36:                  if value == initial_point:
37:                      win = win + 1
38:                      check = False
39:                  elif value == 7:
40:                      lost = lost + 1
41:                      check = False
42:  
43:      # call percent function
44:      percentage = percent(win,lost)
45:      return percentage
46:  
47:  # display number games won and lost and calculate percent won
48:  def percent(win,lost):
49:      print('Number of wins is',win,'Number of lost is', lost)
50:      percent = win/100
51:      return percent
52:  
53:  # call roll function and print percent games won
54:  def main():
55:      # note: I have tried to place the for loop in the main function
56:      # before calling the function roll, however by doing that the results
57:      # display 0 for both the percent and the number of wins
58:      roll = rolling()
59:      print('Your percent games won after 100 games is',roll)
60:  
61:  # call main function
62:  main()
Please enter a file name: number_list
No such file in directory,Please enter another file name: number_list.txt
1:  0
2:  1
3:  2
4:  3
5:  4
6:  5
7:  6
8:  7
9:  8
10:  9
11:  10
12:  11
13:  12
14:  13
15:  14
16:  15
17:  16
18:  17
19:  18
20:  19
21:  20
22:  21
23:  22
24:  23
25:  24
26:  25
27:  26
28:  27
29:  28
30:  29
31:  30
32:  31
33:  32
34:  33
35:  34
36:  35
37:  36
38:  37
39:  38
40:  39
41:  40
42:  41
43:  42
44:  43
45:  44
46:  45
47:  46
48:  47
49:  48
50:  49
51:  50
52:  51
53:  52
54:  53
55:  54
56:  55
57:  56
58:  57
59:  58
60:  59
61:  60
62:  61
63:  62
64:  63
65:  64
66:  65
67:  66
68:  67
69:  68
70:  69
71:  70
72:  71
73:  72
74:  73
75:  74
76:  75
77:  76
78:  77
79:  78
80:  79
81:  80
82:  81
83:  82
84:  83
85:  84
86:  85
87:  86
88:  87
89:  88
90:  89
91:  90
92:  91
93:  92
94:  93
95:  94
96:  95
97:  96
98:  97
99:  98
100:  99
101:  100
Please enter a file name: programming exercise - line number.py
1:  # ask user for file name
2:  # determine if file is in directory
3:  # add number to lines
4:  # create new text file with number in lines
5:  # display file number lines
6:  
7:  # note: I was not able to make my program ignore the
8:  # that start with # or blank spaces
9:  
10:  # open file for reading
11:  def content(file):
12:      file_opened = True
13:      while file_opened:
14:          try:
15:              in_file = open(file, 'r')
16:              file_opened = False
17:          # if file not in directory, prompt for another file
18:          except IOError:
19:              file = input('No such file in directory,'\
20:                           'Please enter another file name: ')
21:      return in_file
22:  
23:  # add number to lines
24:  def read_file(in_file):
25:      # create new file for writing
26:      new_file = open('new_file.txt','w')
27:      # read lines in file
28:      line = in_file.readline()
29:      # set accumulator
30:      line_num = 0
31:      while line != '':
32:          line = line.strip('\n')
33:          line_num = line_num + 1
34:          # display the number lines in screen
35:          print('%d: ' %(line_num),line)
36:          line = in_file.readline()
37:  
38:          # copy number lines into new text file
39:          new_file.write(str(line_num) + str(line))
40:      
41:      new_file.close()
42:  
43:  # prompt for file name and call other functions
44:  def main():
45:      file = input('Please enter a file name: ')
46:      in_file = content(file)
47:      add_number = read_file(in_file)
48:      
49:      in_file.close()
50:  
51:  # call main function
52:  main()

Chapter 8 - Programming Exercise
3)
Phase 1:
Code:
# ask user for date in form mm/dd/yy
# convert to form mm dd,yy
# display date

# convert the date from mm/dd/yy form to mm dd, yy form
def time(date):
    # call convert month function
    new_month = month(date)
    # call remove first dash function
    noDash1 = removeDash1(date)
    # print day
    day = date[3:5]
    # call replace dash to comma function
    comma = changeDash2(date)
    # print year
    year = date[6:10]

    # combine components of the date in new format
    new_date = new_month + noDash1 + day + comma + year
    return new_date

# change numerical value of month to alphabetic word of month
def month(date):
    month_time = date[0:2]
    if '01' in month_time:
        new_month = month_time.replace('01','January')
    elif '02' in month_time:
        new_month = month_time.replace('02','February')
    elif '03' in month_time:
        new_month = month_time.replace('03','March')
    elif '04' in month_time:
        new_month = month_time.replace('04','April')
    elif '05' in month_time:
        new_month = month_time.replace('05','May')
    elif '06' in month_time:
        new_month = month_time.replace('06','June')
    elif '07' in month_time:
        new_month = month_time.replace('07','July')
    elif '08' in month_time:
        new_month = month_time.replace('08','August')
    elif '09' in month_time:
        new_month = month_time.replace('09','September')
    elif '10' in month_time:
        new_month = month_time.replace('10','October')
    elif '11' in month_time:
        new_month = month_time.replace('11','November')
    elif '12' in month_time:
        new_month = month_time.replace('12','December')
    return new_month

# remove first dash
def removeDash1(date):
    dash1 = date[2:3]
    if '/' in dash1:
        no_dash1 = dash1.replace('/',' ')
    return no_dash1

# change second dash to comma
def changeDash2(date):
    dash2 = date[5:6]
    if '/' in dash2:
        replace_dash = dash2.replace('/',', ')
    return replace_dash

# get date from user and display date in new form
def main():
    date = input('Enter a date(mm/dd/yy): ')   
    value = time(date)   
    print('The date you entered is',value)

# call main function
main()

Test Cases:
Enter a date(mm/dd/yy): 09/12/2004
The date you entered is September 12, 2004
Enter a date(mm/dd/yy): 01/26/1980
The date you entered is January 26, 1980
Enter a date(mm/dd/yy): 08/08/2008
The date you entered is August 08, 2008

Phase 2:
Code:
# ask user for date in form mm/dd/yy
# validate date in correct range
# convert to form mm dd,yy
# display date

# determine if number is in correct range
def validate(date):
    # slice date to show only digits for month
    act_month = date[0:2]
    # convert string to integer
    num_month = int(act_month)
    # slice date to show only digits for day
    act_day = date[3:5]
    # convert string to integer
    num_day = int(act_day)
    num = '00'
    # determine if month and day are valid dates within specific range
    if num == '00':
        if num_month == 1 or num_month == 3 or num_month == 5\
           or num_month == 7 or num_month == 8 or num_month == 10\
           or num_month == 12:
            if num_day<=0 or num_day>31:
                return 'Error'
            else:
                return time(date)
        elif num_month == 4 or num_month == 6 or num_month == 9\
           or num_month == 11:
            if num_day<=0 or num_day>30:
                return 'Error'
            else:
                return time(date)
        elif num_month == 2:
            if num_day<=0 or num_day>28:
                return 'Error'
            else:
                return time(date)
        elif num_month<=0 or num_month>12:
            return 'Error'
        else:
            return time(date)
        
# convert the date from mm/dd/yy form to mm dd, yy form
def time(date):
    # call convert month function
    new_month = month(date)
    # call remove first dash function
    noDash1 = removeDash1(date)
    # print day
    day = date[3:5]
    # call replace dash to comma function
    comma = changeDash2(date)
    # print year
    year = date[6:10]

    new_date = new_month + noDash1 + day + comma + year
    return new_date

# change numerical value of month to alphabetic word of month
def month(date):
    month_time = date[0:2]
    if '01' in month_time:
        new_month = month_time.replace('01','January')
    elif '02' in month_time:
        new_month = month_time.replace('02','February')
    elif '03' in month_time:
        new_month = month_time.replace('03','March')
    elif '04' in month_time:
        new_month = month_time.replace('04','April')
    elif '05' in month_time:
        new_month = month_time.replace('05','May')
    elif '06' in month_time:
        new_month = month_time.replace('06','June')
    elif '07' in month_time:
        new_month = month_time.replace('07','July')
    elif '08' in month_time:
        new_month = month_time.replace('08','August')
    elif '09' in month_time:
        new_month = month_time.replace('09','September')
    elif '10' in month_time:
        new_month = month_time.replace('10','October')
    elif '11' in month_time:
        new_month = month_time.replace('11','November')
    elif '12' in month_time:
        new_month = month_time.replace('12','December')
    return new_month

# remove first dash
def removeDash1(date):
    dash1 = date[2:3]
    if '/' in dash1:
        no_dash1 = dash1.replace('/',' ')
    return no_dash1

# change second dash to comma
def changeDash2(date):
    dash2 = date[5:6]
    if '/' in dash2:
        replace_dash = dash2.replace('/',', ')
    return replace_dash

# get date from user and display date in new form
def main():
    date = input('Enter a date(mm/dd/yy): ')
    valid = validate(date)
    print(valid)

# call main function
main()

Test Cases:
Enter a date(mm/dd/yy): 15/09/1975
Error
Enter a date(mm/dd/yy): 08/36/2009
Error
Enter a date(mm/dd/yy): 03/18/2000
March 18, 2000
Enter a date(mm/dd/yy): 06/11/1895
June 11, 1895
Enter a date(mm/dd/yy): 05/20/1945
May 20, 1945

Phase 3:
Code:
# ask user for date in form mm/dd/yy
# determine correct format
# determine correct range of date
# convert to form mm dd,yy
# display date

# determine correct format
def formatting(date):
    length = len(date)
    # slice date to find first dash
    dashy1 = date[0:4]
    act_dash1 = dashy1.find('/')
    # slice date to find second dash
    dashy2 = date[4:10]
    act_dash2 = dashy2.find('/')

    # set boolean variables
    has_digit = False
    correct_length = False
    correct_dash1 = False
    correct_dash2 = False

    # determine if date in correct format
    if length == 10:
        correct_length = True

        for ch in date:
            if ch.isdigit():
                has_digit = True
        for ch1 in dashy1:
            if act_dash1 == 2:
                correct_dash1 = True
        for ch2 in dashy2:
            if act_dash2 == 1:
                correct_dash2 = True

    # if date meet requirements convert date format
    if correct_length and has_digit and \
       correct_dash1 and correct_dash2:
        return validate(date)
    else:
        return 'Error'

# determine if number is in correct range
def validate(date):
    act_month = date[0:2]
    num_month = int(act_month)
    act_day = date[3:5]
    num_day = int(act_day)
    num = '00'
    if num == '00':
        if num_month == 1 or num_month == 3 or num_month == 5\
           or num_month == 7 or num_month == 8 or num_month == 10\
           or num_month == 12:
            if num_day<=0 or num_day>31:
                return 'Error'
            else:
                return time(date)
        elif num_month == 4 or num_month == 6 or num_month == 9\
           or num_month == 11:
            if num_day<=0 or num_day>30:
                return 'Error'
            else:
                return time(date)
        elif num_month == 2:
            if num_day<=0 or num_day > 28:
                return 'Error'
            else:
                return time(date)
        elif num_month<=0 or num_month>12:
            return 'Error'
        else:
            return time(date)
        
# convert the date from mm/dd/yy form to mm dd, yy form
def time(date):
    # call convert month function
    new_month = month(date)
    # call remove first dash function
    noDash1 = removeDash1(date)
    # print day
    day = date[3:5]
    # call replace dash to comma function
    comma = changeDash2(date)
    # print year
    year = date[6:10]

    new_date = new_month + noDash1 + day + comma + year
    return new_date

# change numerical value of month to alphabetic word of month
def month(date):
    month_time = date[0:2]
    if '01' in month_time:
        new_month = month_time.replace('01','January')
    elif '02' in month_time:
        new_month = month_time.replace('02','February')
    elif '03' in month_time:
        new_month = month_time.replace('03','March')
    elif '04' in month_time:
        new_month = month_time.replace('04','April')
    elif '05' in month_time:
        new_month = month_time.replace('05','May')
    elif '06' in month_time:
        new_month = month_time.replace('06','June')
    elif '07' in month_time:
        new_month = month_time.replace('07','July')
    elif '08' in month_time:
        new_month = month_time.replace('08','August')
    elif '09' in month_time:
        new_month = month_time.replace('09','September')
    elif '10' in month_time:
        new_month = month_time.replace('10','October')
    elif '11' in month_time:
        new_month = month_time.replace('11','November')
    elif '12' in month_time:
        new_month = month_time.replace('12','December')
    return new_month

# remove first dash
def removeDash1(date):
    dash1 = date[2:3]
    if '/' in dash1:
        no_dash1 = dash1.replace('/',' ')
    return no_dash1

# change second dash to comma
def changeDash2(date):
    dash2 = date[5:6]
    if '/' in dash2:
        replace_dash = dash2.replace('/',', ')
    return replace_dash

# get date from user and display date in new form
def main():
    date = input('Enter a date(mm/dd/yy): ')
    right_format = formatting(date)
    print(right_format)

# call main function
main()

Test Cases:
Enter a date(mm/dd/yy): 042/1/2210
Error
Enter a date(mm/dd/yy): 421580241
Error
Enter a date(mm/dd/yy): 09/281/982
Error
Enter a date(mm/dd/yy): 02/28/2000
February 28, 2000
Enter a date(mm/dd/yy): 07/08/1942
July 08, 1942

Phase 4:
Code:
# ask user for date in form mm/dd/yy
# determine correct format
# determine correct range of date
# convert to form mm dd,yy
# display date

# determine correct format
def formatting(date):
    length = len(date)
    # slice date to find first dash
    dashy1 = date[0:4]
    act_dash1 = dashy1.find('/')
    # slice date to find second dash
    dashy2 = date[4:10]
    act_dash2 = dashy2.find('/')

    # set boolean variables
    has_digit = False
    correct_length = False
    correct_dash1 = False
    correct_dash2 = False

    # determine if date in correct format
    if length == 10:
        correct_length = True

        for ch in date:
            if ch.isdigit():
                has_digit = True
        for ch1 in dashy1:
            if act_dash1 == 2:
                correct_dash1 = True
        for ch2 in dashy2:
            if act_dash2 == 1:
                correct_dash2 = True
    # if date meet all requirements convert date format
    if correct_length and has_digit and \
       correct_dash1 and correct_dash2:
        return validate(date)
    else:
        return 'Error'

# determine if number is in correct range
def validate(date):
    act_month = date[0:2]
    num_month = int(act_month)
    act_day = date[3:5]
    num_day = int(act_day)
    num = '00'
    if num == '00':
        if num_month == 1 or num_month == 3 or num_month == 5\
           or num_month == 7 or num_month == 8 or num_month == 10\
           or num_month == 12:
            if num_day<=0 or num_day>31:
                return 'Error'
            else:
                return time(date)
        elif num_month == 4 or num_month == 6 or num_month == 9\
           or num_month == 11:
            if num_day<=0 or num_day>30:
                return 'Error'
            else:
                return time(date)
        elif num_month == 2:
            if num_day<=0 or num_day>28:
                return 'Error'
            else:
                return time(date)
        elif num_month<=0 or num_month>12:
            return 'Error'
        else:
            return time(date)
        
# convert the date from mm/dd/yy form to mm dd, yy form
def time(date):
    # call convert month function
    new_month = month(date)
    # call remove first dash function
    noDash1 = removeDash1(date)
    # print day
    day = date[3:5]
    # call replace dash to comma function
    comma = changeDash2(date)
    # print year
    year = date[6:10]

    new_date = new_month + noDash1 + day + comma + year
    return new_date

# change numerical value of month to alphabetic word of month
def month(date):
    new_month = ''
    month_time = date[0:2]
    if '01' in month_time:
        new_month = month_time.replace('01','January')
    elif '02' in month_time:
        new_month = month_time.replace('02','February')
    elif '03' in month_time:
        new_month = month_time.replace('03','March')
    elif '04' in month_time:
        new_month = month_time.replace('04','April')
    elif '05' in month_time:
        new_month = month_time.replace('05','May')
    elif '06' in month_time:
        new_month = month_time.replace('06','June')
    elif '07' in month_time:
        new_month = month_time.replace('07','July')
    elif '08' in month_time:
        new_month = month_time.replace('08','August')
    elif '09' in month_time:
        new_month = month_time.replace('09','September')
    elif '10' in month_time:
        new_month = month_time.replace('10','October')
    elif '11' in month_time:
        new_month = month_time.replace('11','November')
    elif '12' in month_time:
        new_month = month_time.replace('12','December')
    return new_month

# remove first dash
def removeDash1(date):
    dash1 = date[2:3]
    if '/' in dash1:
        no_dash1 = dash1.replace('/',' ')
    return no_dash1

# change second dash to comma
def changeDash2(date):
    dash2 = date[5:6]
    if '/' in dash2:
        replace_dash = dash2.replace('/',', ')
    return replace_dash

# open date file for reading
# display new date format or error
def main():
    date = open('dates.txt','r')
    line = date.readline()

    while line != '':
        new_line = line.strip('\n')
        right_format = formatting(new_line)     
        print(right_format)
        line = date.readline()
        
    date.close()

# call main function
main()

Test Cases:
March 16, 2009
December 25, 1975
February 28, 2000
Error
Error
July 31, 1867
Error
Error
Error
Error
Error
Error
Error
Error
Error
Error
