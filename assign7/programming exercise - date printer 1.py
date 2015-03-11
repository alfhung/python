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
            new_month == month_time.replace('03','March')
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
