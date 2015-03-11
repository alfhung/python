# ask user for file name
# determine if file is in directory
# add number to lines
# create new text file with number in lines
# display file number lines

# note: I was not able to make my program ignore the
# that start with # or blank spaces

# open file for reading
def content(file):
    file_opened = True
    while file_opened:
        try:
            in_file = open(file, 'r')
            file_opened = False
        # if file not in directory, prompt for another file
        except IOError:
            file = input('No such file in directory,'\
                         'Please enter another file name: ')
    return in_file

# add number to lines
def read_file(in_file):
    # create new file for writing
    new_file = open('new_file.txt','w')
    # read lines in file
    line = in_file.readline()
    # set accumulator
    line_num = 0
    while line != '':
        line = line.strip('\n')
        line_num = line_num + 1
        # display the number lines in screen
        print('%d: ' %(line_num),line)
        line = in_file.readline()

        # copy number lines into new text file
        new_file.write(str(line_num) + str(line))
    
    new_file.close()

# prompt for file name and call other functions
def main():
    file = input('Please enter a file name: ')
    in_file = content(file)
    add_number = read_file(in_file)
    
    in_file.close()

# call main function
main()
