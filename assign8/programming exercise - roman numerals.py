# prompt user for input
# validate input is integer and within range
# convert decimal to Roman
# display Roman

# validate user input, prompt for new entry if not valid
def validate(entry):
    validation = False
    while validation == False:
        if entry.isdigit() == True:
            num = int(entry)
            if num >= 1 and num <= 10:
                validation = True
            else:
                entry = input('Your number must be an integer ' \
                              'between 1 and 10 (inclusive),' \
                              'Please enter a new number: ')
        else:
            if entry.isdigit() != True:
                entry = input('Your number must be an integer ' \
                              'between 1 and 10 (inclusive),' \
                              'Please enter a new number: ')
    return entry

# convert decimal to Roman
def conversion(entry):
    romans = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
    value = romans[int(entry)-1]
    return value

# get user input
def main():
    entry = input('Please enter a number: ')
    keep_entering = 'y'
    while keep_entering == 'y':
        valid = validate(entry)
        new_entry = int(valid)
        roman = conversion(entry)
        print('Your roman number of %d is %s' %(new_entry,roman))
        keep_entering = input('Do you want to keep converting? '\
                              'Enter y (yes) or n (no): ')
        entry = input('Please enter another number: ')

# call main function
main()
