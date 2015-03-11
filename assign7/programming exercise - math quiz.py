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
