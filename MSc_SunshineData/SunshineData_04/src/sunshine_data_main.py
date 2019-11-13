__author__ = 'Jane'
'''
Tasks:
1 - Take a look at file_reader.py: note the simplicity, the docstrings and the comments
2 - There are three runtime errors in the function adding sunshine data, what are they?
    How could you find them? Should you be testing for them...? (Hint: the answer is YES!!!)
3 - How are those print() calls working in lines 53 and 55?
'''
# -------------------------------------------------------------------------------
# Name:        SunshineData_main
# Purpose:     Demonstration for MSc welcome week
#
# Author:      Jane Lewis xw904346
#
# Created:     25/08/2015
# Copyright:   (c) xw904346 2015
# -------------------------------------------------------------------------------

"""
NAME
   SunshineData_main - Main program to run analysis on sunshine data file
FILE
   sunshine_data_main.py

FUNCTIONS
   add_sunshine_per_day(...)
       Iterate over hourly sunshine data and accumulate total daily hours.

"""
# TODO runtime options
# option: take file name from command line argument
import file_reader
import numpy as np

def add_sunshine_per_day(file_contents):
    """

    :param file_contents:
    :return:
    """
    # We need to add up sunshine hours for each day and create a new data store to hold the results
    sunshine_hours = list()
    # So first, get the first row and its date, put its sunshine hours in an accumulator
    current_date = file_contents[0]['UTC'].date()
    hours = file_contents[0]['h']
    print(len(file_contents))
    # loop through the data, row by row
    # we can do this with a counter which goes from 2nd to the end (don't forget indexes start at 0 though)
    for counter in range(1, len(file_contents)):
        # Get the date, and get each subsequent one until it changes, adding up the hours as we go along
        next_date = file_contents[counter]['UTC'].date()
        if next_date == current_date:
            print(str(file_contents[counter]['h']) + ' individual')
            hours += file_contents[counter]['h']
            print(str(hours) + ' accumulated')
        else:  # we've gone onto the next day
            # let's store the information in a list
            temp_data = (current_date, hours)
            # and add the sub list to the main one
            sunshine_hours.append(temp_data)
            # reset the accumulator
            hours = 0
    print(sunshine_hours)

def main():
    # set file path/name here not in the reader, so it's easier to change later
    filename = '..\..\MODE3_2015-08-25_2014-09-01_2015-08-25_d447917LU.csv'
    # call FileReader.loadFile(filepath) to return data in suitable variables
    file_contents = file_reader.loadfile(filename)
    # use functions here to process data
    add_sunshine_per_day(file_contents)
    # send processed data to Plotting.* methods to draw graphs
    # else:
    # call methods in tests.py

if __name__ == '__main__':
    main()




