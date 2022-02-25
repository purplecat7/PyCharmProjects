__author__ = 'Jane'
"""
Tasks:
1 - 6 inline
NOTE: file header and docstring
"""
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

import csv

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
        extracted_data = read_csv_file(filename)
    # etc.
    return extracted_data

def read_csv_file(filename):
    '''
    Function to read a csv format file
    :param: filename: full filepath to csv file (string)
    :returns: ???
    :raise: runtime exception
    '''

    # 1 - What is the error when you run this line of code? What needs to be done?
    # csv_reader = csv.reader(filename)

    # 2 - Comment out the code above and run with this instead. What goes wrong now?
    file_contents = open(filename)
    csv_reader = csv.reader(file_contents)

    for row in csv_reader:
        print (row)
    # 3 - if you want an accumulator you must initialise it first. But there's now a new error - what is it and why?
        sunnysec = 0
        radtotal = 0
    # 4 - Note that we can use an inbuilt function to test for row length. Get the help on this to see its definition.
        if (len(row) < 5):
    # 5 - Exceptions are very useful but require discipline to use. Never scatter them about without a plan!
    #     What is the ','.join() function doing? Can you find the help for it?
            raise RuntimeError('Expected row in the form <date>,<hour>,<sunny(sec)>,<sunny(total)>,<solar_rad> but got ' + ','.join(row))
        date = row[0]
        hour = row[1]
        sunnysec += row[2]
        sunnytotal = row[3]
        radtotal += row[4]

    # 6 - Consider the design issues of processing the data in the same place as reading it...





# Answers:
# 1 - You can't iterate over csv_reader as it's not actually loaded anything in - check its documentation
# 2 - The row you get is the headers so no good for anything!
# 3 - Initialising the accumulator inside the loop means you won't actually accumulate anything
# 4 - Just have a look
# 5 - Using the incorrect (first) attempt at csv_reader, you'll see this error
# 6 - Really not a good idea