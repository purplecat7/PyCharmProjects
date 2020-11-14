__author__ = 'Jane'
'''
Tasks:
1 - 6 inline
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

import csv

def loadfile(filename):

    """
    Reads a csv format file.

    Args:
        filename: full filepath to csv file (string)

    Raises:
        generic runtime exception with notification to user

    """

    # 1 - What is the error when you run this code? What needs to be done?
    #csv_reader = csv.reader(filename)

    # 2 - Comment out the code above and run with this instead. What goes wrong now?
    file_contents = open(filename)
    csv_reader = csv.reader(file_contents)

    for row in csv_reader:
        print (row)
    # 3 - so if you want an accumulator you must initialise it first. But there's now a new error - what is it and why?
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
