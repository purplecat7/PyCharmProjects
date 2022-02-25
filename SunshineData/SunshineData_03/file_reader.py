__author__ = 'Jane'
'''
Tasks:
Run the program and call read_csv_file1, 2 & 3 in turn.
1 - 3 in read_csv_file1() function
4 - 8 in read_csv_file2() function
9 - 13 in read_csv_file3() function
'''
# -------------------------------------------------------------------------------
# Name:        FileReader
# Purpose:     Exercise for Scenario/DTP training.
#
# Author:      Jane Lewis to104469
#
# Created:     25/08/2015
# Copyright:   (c) to104469 2015
# -------------------------------------------------------------------------------

"""
NAME
   FileReader - Given file details, open and read the data into suitable variables to pass back
FILE
   file_reader.py

FUNCTIONS
   loadfile(...)
       Open and read a file given its name and location

"""
import numpy as np
import datetime as dt

def loadfile(filename):
    '''
    Main entry function which takes any file type and calls appropriate specific loader.
    :param: filename: full filepath to data file (string)
    :returns: loaded data as 2D array
    '''
    # use 'if' statements to see what the filename extension is and then pass on the actual reading to a
    # dedicated function.
    # this is an example of a 'wrapper' function... the calling function, main(), defers responsibility to this
    # function to sort out how the file is read so doesn't need to know about different formats itself.
    # if it's csv
    if str(filename).endswith('csv'):
        extracted_data = read_csv_file1(filename)
        # extracted_data = read_csv_file2(filename)
        # extracted_data = read_csv_file3(filename)
    # etc.
    return extracted_data

def read_csv_file1(filename):
    '''
    Function to read a csv format file
    :param: filename: full filepath to csv file (string)
    :returns: 2D array of file data without header lines
    :raise: runtime exception
    '''
    # 1 - We've given up on csv.file_reader, it's clunky and there are better options
    # Examine the output from this numpy function and see if it's what we're after
    # (remember to look it up the help to give you a few clues)
    file_contents = np.genfromtxt(filename, delimiter=',', skip_header=2)

    # 2 - What if we try this instead? What does the 'dtype' argument do?
    # (comment out line 56, and uncomment the one below)
    file_contents = np.genfromtxt(filename, dtype=None, delimiter=',', skip_header=2)

    print(len(file_contents))

    # 3 - Can you explain this syntax?
    print(file_contents[0])
    for item in file_contents[0]:
        print(item)

    return file_contents


def read_csv_file2(filename):
    file_contents = np.genfromtxt(filename, dtype=None, delimiter=',', skip_header=2)
    #new_contents = list()

    # 4 - Look up the datetime type in the help; what advantages does it confer to use this type instead of keeping
    # the data as strings or numbers?
    # We need to sort out the date and time datatypes - column1 is date, column2 is time

    # Let's iterate through each line
    for line in file_contents:
        print (line)
        # Now let's make column1 into a date - we need to convert the integer into a string so we can slice bits out,
        # then turn it back into an integer to be acceptable to the dt.date method!
        mydate = dt.date(int(str(line[0])[:4]),
                         int(str(line[0])[4:6]),
                         int(str(line[0])[6:]))
        print(mydate)
        # And the same for column2 into a time
        mytime = dt.time(int(str(line[1])[:2]))
        print (mytime)

    # 5 - Can we substitute it back? What happens?
    # Uncomment the following two lines
    #     line[0] = mydate
    #     line[1] = mytime

        # But this is all getting quite hard now...
        # Perhaps we should have tried the 'strptime' method
        # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    # 6 - uncomment these next four lines of code and see what happens (you'll need to comment out lines 89-90 above)
    # Can you explain the error?
        #mydate = dt.datetime.strptime(line[0],'%Y%m%d')
        #mytime = dt.datetime.strptime(line[1],'%H%M')
        #print(mydate)
        #print(mytime)

    # 7 - So we should give up on that, it's not helping. Instead, let's recreate the data rather than trying to
    # substitute it, comment out the strptime() attempt above, and uncomment 112, 113, 117 below
    # We're trying to use a new holder for the data though, to it'll need to be declared first...
    # find the line to uncomment.
        #newline = (mydate, mytime, line[2], line[3], line[4])
        #new_contents.append(newline)

    # 8 - Now there's another error, what is it, where does it happen, and why?
    # Hint: leading zeros...
    #print (new_contents)

    # WE REALLY ARE GOING ABOUT THIS THE WRONG WAY, WHY NOT INGEST THE RIGHT TYPES STRAIGHT OFF?

def read_csv_file3(filename):
    # Let's look this up and hatch a better plan:
    # http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html
    # We'll use the 'names' facility by reading line 2 of the data,
    # and we'll specify each 'dtype' too.
    file_contents = np.genfromtxt(filename, dtype=(dt.date, dt.time, np.int16, np.float16, np.float32),
                                  delimiter=',', skip_header=1, names=True)

    # 9 - These next three lines show you the types of each element in the first line of data and the contents.
    # Using this as an example, print out the types of the first two elements of the fifth line, and the contents
    # of the 14th to 20th (inclusive) line of data. Check you have the right answers by looking at the source .csv file.
    for n in range(0,5):
        print(type(file_contents[0][n]))
    print(file_contents[0])

    # this is handy for separating output, not to be left in the finished code!
    print ('------------------')

    # 10 - What are the types of our dates and times? Is this right?

    # 11 - Run the rest of this code and check the results. Try querying the loaded data in 'file_contents'
    # We should use the 'converters' argument available in genfromtxt() but this also means we have to make sure
    # we know where to apply it: this makes use of the 'names' argument - look up what it does.
    # (see http://stackoverflow.com/questions/13869966/numpy-genfromtxt-with-datetime-strptime-converter)
    convertdatefunc = lambda x: dt.datetime.strptime(x, '%Y%m%d')
    converttimefunc = lambda y: dt.datetime.strptime(y, '%H%M')
    # 12 - we need to convert the bytes so that strptime() will work. Comment out the two lines above and use
    # the two below instead.
    # convertdatefunc = lambda x: dt.datetime.strptime(x.decode("utf-8"), '%Y%m%d')
    # converttimefunc = lambda y: dt.datetime.strptime(y.decode("utf-8"), '%H%M')
    file_contents = np.genfromtxt(filename, dtype=(dt.datetime, dt.datetime, np.int16, np.float16, np.float32),
                                  delimiter=',', skip_header=1, names=True,
                                  converters={"UTC":convertdatefunc, "hhmm":converttimefunc})
    # 13 - BUT WHAT'S NOTICEABLY NOT GOOD ABOUT THIS from a design point of view?

    # Let's just check it's what we're expecting
    for n in range(0,5):
        print(type(file_contents[0][n]))
    print(file_contents[0])
    print(file_contents[3][0])
    print(file_contents[3][0].date())
    print(file_contents[10][1].time().hour)
    print(file_contents[10][1].time().minute)
    # and also, because we named the columns, we can use this:
    print(file_contents[3]['UTC'].date())
    print(file_contents[10]['hhmm'].time().hour)
    print(file_contents[10]['hhmm'].time().minute)

    # Send the data back to the calling function
    return file_contents








# Answers:
# 1 - Well it's a nice 2D array but everything is to 5 decimal places including the date!
# 2 - It's an array of tuples, and it's all numbers without decimal padding
# 3 - We're getting the first element, then iterating through its contents
# 4 - Given we have the contents, now we're trying to get them in the right format and datetime is the way to go.
#     Slice up the date portion, and the time portion - but the leading zero has gone so 0100 ends up as 10am
# 5 - Since we have a tuple, no we cannot write it back... tuples are immutable
# 6 - strptime() does not work on numbers, only on strings
# 7 - Uncomment line 74
# 8 - There's an exception as soon as an hour isn't 0..23, and that's because we lost the leading zero.
# 9 - type(file_contents[4][0]) and type(file_contents[4][1])
#     for n in range(14, 21): print(file_contents[n])
# 10- They're byte objects and no, that's not what we want
# 11- Trying to use the converters on the byte objects fails so we will need to convert into a string
# 12- It should now work.
# 13- There are hard-coded column names.