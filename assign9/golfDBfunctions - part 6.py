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
