# ask user for name of file
# confirm file exist
# open file for reading
# read content in file
# read a sentence
    # accumulate words
    # take average words in sentence
    # add number to list
    # read next sentence, do same until end document
# add total in list, then average

# confirm file exist, if not prompt for new file name
def validation(file):
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

# read content in file, count words in sentence
# get average words from each sentence, add to a list
# get final average word
def content(valid):
    line = valid.readline()
    avg_list = []
    total_word_sentence = 0
    while line != '':
        line = line.rstrip('\n')
        line_list = line.split('.')
        # count words in sentence
        for word in line_list:
            count = counting(line)
            avg_sen_word = count/len(line_list)
            avg_list.append(avg_sen_word)

    sum_avg = 0
    for num in avg_list:
        sum_avg = sum_avg + num

    average_words = sum_avg/len(avg_list)
    return average_word

# get total words in sentence
def counting(line):
    item_list = line.split(' ')
    number_word = len(item_list)
    return number_word

# prompt user for file name
def main():
    file = input('Please enter file name: ')
    valid = validation(file)
    totaling = content(valid)
    print(totaling)

    valid.close()

# call main function
main()
