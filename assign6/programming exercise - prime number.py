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
