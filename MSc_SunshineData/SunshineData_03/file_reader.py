__author__ = 'Jane'
'''
Tasks:
1 - 3 in loadfile1() function
4 - 8 in loadfile2() function
9 - 12 in loadfile3() function
'''
# -------------------------------------------------------------------------------
# Name:        FileReader
# Purpose:     Demonstration for MSc welcome week
#
# Author:      Jane Lewis xw904346
#
# Created:     25/08/2015
# Copyright:   (c) xw904346 2015
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

def loadfile1(filename):

    """
    Reads a csv format file.

    Args:
        filename: full filepath to csv file (string)

    Returns:
        2D array of file data without header lines

    Raises:
        generic runtime exception with notification to user

    """
    # 1 - We've given up on csv.file reader, it's clunky and there are better options
    # Examine the output from this numpy function and see if it's what we're after
    # (remember to look it up the help to give you a few clues)
    file_contents = np.genfromtxt(filename, delimiter=',', skip_header=2)

    # 2 - What if we try this instead? What does the 'dtype' argument do?
    # (comment out line 50, and uncomment the one below)
    #file_contents = np.genfromtxt(filename, dtype=None, delimiter=',', skip_header=2)

    print(len(file_contents))

    # 3 - Can you explain this syntax?
    print(file_contents[0])
    for item in file_contents[0]:
        print(item)

    return file_contents


def loadfile2(filename):
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
        #line[0] = mydate
        #line[1] = mytime

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
    # substitute it, comment out lines 97-98 above, and uncomment 106-107, 111
    # We're trying to use a new holder for the data though, to it'll need to be declared first...
    # find the line to uncomment.
        #newline = (mydate, mytime, line[2], line[3], line[4])
        #new_contents.append(newline)

    # 8 - Now there's another error, what is it, where does it happen, and why?
    # Hint: leading zeros...
    #print (new_contents)

    # WE REALLY ARE GOING ABOUT THIS THE WRONG WAY, WHY NOT INGEST THE RIGHT TYPES STRAIGHT OFF?

def loadfile3(filename):
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

    # 11 - uncomment the rest of this code and check the results. Try querying the loaded data in 'file_contents'
    # We should use the 'converters' argument available in genfromtxt() but this also means we have to make sure
    # we know where to apply it: this makes use of the 'names' argument - look up what it does.
    # (see http://stackoverflow.com/questions/13869966/numpy-genfromtxt-with-datetime-strptime-converter)
    convertdatefunc = lambda x: dt.datetime.strptime(x,'%Y%m%d')
    converttimefunc = lambda y: dt.datetime.strptime(y,'%H%M')
    file_contents = np.genfromtxt(filename, dtype=(dt.datetime, dt.datetime, np.int16, np.float16, np.float32),
                                  delimiter=',', skip_header=1, names=True,
                                  converters={"UTC":convertdatefunc, "hhmm":converttimefunc})
    # 12 - BUT WHAT'S NOTICEABLY NOT GOOD ABOUT THIS from a design point of view?

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