Assignment 6

Part I:
Chapter 6 - Algorithm Workbench
1)
import random

rand = random.randrange(1,101)

Chapter 5 - Algorithm Workbench
1)
numb = int(input('Please enter a number: '))
product = numb * 10

while product < 100:
    print(product)
    
    numb = int(input('Enter another number: '))
    product = numb * 10

2)
value = 1
add = 0
go = 'yes'

while go=='yes':
	numb1 = int(input('Please enter the first number: '))
	numb2 = int(input('Please enter the second number: '))
	sum = numb1 + numb2
	print(sum)

	go = input('Continue another operation?' \
                   '(Enter yes if you want to continue): ')

7)
for row in range(10):
    print('')
    for column in range(15):
        print('#', end = '')

9)
num = int(input('Please enter a number: '))

while num < 1 or num > 100:
    print('Number is out of range(1-100),'\
          'please enter a number in range of 1-100')
    num = int(input('Enter a new number: '))

Part II:
Chapter 6 - Programming Exercise
2)
Code:
# create math quiz from two random integers 
# add the two integers
# get answers from user
# determine if answer is correct
# display the percent correct

# import functions from random module
import random

# add the two random numbers
def add(numb1,numb2):
    calculate = int(numb1 + numb2)
    return calculate

# get answer from user, validate answer and accumulate right answers
def decide(numb1,numb2):
    right = 0
    # run loop 5 times and accumulate number of correct answers
    for oper in range (5):
        # note: since exercise ask to write program that gives simple math quizzes
        # I decided to select the range of random numbers to be between 1 and 1000
        numb1 = random.randint(1,1000)
        numb2 = random.randint(1,1000)
        answer = int(input('Please enter the answer to %d + %d: ' %(numb1,numb2)))

        # validates answer
        while answer < 0:
            print('Answer is positive')
            answer = int(input('Enter a new answer: '))

        # call add function to perform addition
        ad = add(numb1,numb2)

        # determine if answer is correct or wrong
        if answer == ad:
            right = right + 1
            print('Congratulations! Your answer is correct.')
        else:
            print('Your answer is wrong, the correct answer is %d.' %(ad))

    # call percent function
    percentage = percent(right)

# determine and print percent correct
def percent(right):
    if right == 0:
        print('You answered 0/5 questions correct, your score is 0')
    elif right == 1:
        print('You answered 1/5 question correct, your score is 20')
    elif right == 2:
        print('You answered 2/5 questions correct, your score is 40')
    elif right == 3:
        print('You answered 3/5 questions correct, your score is 60')
    elif right == 4:
        print('You answered 4/5 questions correct, your score is 80')
    elif right == 5:
        print('You answered 5/5 questions correct, your score is 100')
        
# defina random integers and call other functions
def main():
    numb1 = 0
    numb2 = 0
	
    addition = add(numb1,numb2)
    correct = decide(numb1,numb2)

# call main function
main()

Test Cases:
Please enter the answer to 359 + 90: 449
Congratulations! Your answer is correct.
Please enter the answer to 264 + 792: -1024
Answer is positive
Enter a new answer: 1025
Your answer is wrong, the correct answer is 1056.
Please enter the answer to 982 + 760: 1692
Your answer is wrong, the correct answer is 1742.
Please enter the answer to 137 + 519: 656
Congratulations! Your answer is correct.
Please enter the answer to 703 + 162: 865
Congratulations! Your answer is correct.
You answered 3/5 questions correct, your score is 60
Please enter the answer to 452 + 194: 650
Your answer is wrong, the correct answer is 646.
Please enter the answer to 509 + 872: 1381
Congratulations! Your answer is correct.
Please enter the answer to 14 + 877: 891
Congratulations! Your answer is correct.
Please enter the answer to 826 + 526: 1352
Congratulations! Your answer is correct.
Please enter the answer to 800 + 686: -1486
Answer is positive
Enter a new answer: 1486
Congratulations! Your answer is correct.
You answered 4/5 questions correct, your score is 80
Please enter the answer to 667 + 801: 1468
Congratulations! Your answer is correct.
Please enter the answer to 359 + 463: 824
Your answer is wrong, the correct answer is 822.
Please enter the answer to 508 + 778: 1282
Your answer is wrong, the correct answer is 1286.
Please enter the answer to 442 + 236: 679
Your answer is wrong, the correct answer is 678.
Please enter the answer to 556 + 105: 661
Congratulations! Your answer is correct.
You answered 2/5 questions correct, your score is 40

Programming Exercise
1)
Code:
# ask user to input a number
# validate input - determine if entry is bigger than 2
# determine if entry is a prime number
# display if number is prime or nonprime

# import square root function from math module
import math

# validate user input
def validate(number):
    while number <= 2:
        print('Your number must be greater than 2, '\
              'please enter a new number.')

        # obtain new number is number is smaller than 2
        number = int(input('Enter a new number: '))

# determine if number is prime
def isPrime(number):
    value = int(math.sqrt(number))

    # if number is even and divisable by 2, number is not prime
    if number%2 == 0:
        print('Your number is not prime')
        return False
    
    # test if odd number is multiple of any other prime and nonprime numbers
    for num in range(3,value+1,2):
        if number % num == 0:
            print('Your number is not prime')
            return False
    print('Your number is prime')
    return True
    
# obtain number from user
def main():
    number = int(input('Please enter a number: '))
    valid = validate(number)
    
    prime = isPrime(number)

# call main function
main()

Test Cases:
Please enter a number: 83
Your number is prime
Please enter a number: 1
Your number must be greater than 2, please enter a new number.
Enter a new number: 139
Your number is prime
Please enter a number: 5
Your number is prime

2)
Code:
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

Test Cases:
Number of wins is 38 Number of lost is 62
Your percent games won after 100 games is 0.38
Number of wins is 51 Number of lost is 49
Your percent games won after 100 games is 0.51
Number of wins is 43 Number of lost is 57
Your percent games won after 100 games is 0.43
Number of wins is 42 Number of lost is 58
Your percent games won after 100 games is 0.42
