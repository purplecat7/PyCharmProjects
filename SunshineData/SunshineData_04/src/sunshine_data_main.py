__author__ = 'Jane'
'''
Tasks:
1 - Take a look at file_reader.py: note the simplicity, the docstrings and the comments
2 - There are three runtime errors in the function adding sunshine data, what are they?
    How could you find them? Should you be testing for them...? (Hint: the answer is YES!!!)
3 - How are those print() calls working in lines 53 and 55?
4 - How could you avoid having hard-coded strings for columns names in multiple places? What if there was a change?
'''
# -------------------------------------------------------------------------------
# Name:        SunshineData_main
# Purpose:     Exercise for Scenario/DTP training.
#
# Author:      Jane Lewis to104469
#
# Created:     25/08/2015
# Copyright:   (c) to104469 2015
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
# TODO runtime options: filename, variable, operation, plot_type

import os
import file_reader

def add_sunshine_per_day(file_contents):
    """
    Function to process the extracted data. It will sum each day's sunshine hours
    :param file_contents: file contents accessible in a #TODO data type
    :return: summed data as a #TODO data type
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
            print(f"{str(hours)} accumulated")
        else:  # we've gone onto the next day
            # let's store the information in a list
            temp_data = (current_date, hours)
            # and add the sub list to the main one
            sunshine_hours.append(temp_data)
            # reset the accumulator
            hours = 0
    print(sunshine_hours)

def main(filename):
    # TODO def main(filename, ecv, operation, plot_type):
    '''
    Function to create a plot from a data file with user specified calculations and climate variable.
    :param filename: fully qualified file name of the input data
    :param ecv: the name of the climate variable to operate on
    :param operation: the operation to carry out, may be one of 'average' or 'summation'
    :param plot_type: the type of plot to produce, may be one of 'bar', 'line' or 'pie'
    :return: no return
    '''
    # call FileReader.loadFile(filepath) to return data in a suitable variable
    # TODO extracted_data = readfile(filename, ecv)
    file_contents = file_reader.loadfile(filename)
    # use functions here to process data
    hours_per_day = add_sunshine_per_day(file_contents)
    # send processed data to Plotting.* methods to draw graphs

if __name__ == '__main__':
    # set file path/name here not in the reader, so it's easier to change later
    filename = str(
        os.getcwd() + os.sep + '..' + os.sep + '..' + os.sep + 'MODE3_2015-08-25_2014-09-01_2015-08-25_d447917LU.csv')
    main(filename)








# Answers:
# 1 - Better than our initial attempts!
# 2 - (1) We don't want missing values denoted by 9999.9
#     (2) We must not reset the accumulator and lose the existing row
#     (3) Reset the date comparison variable
#     You should write a file (or snip a bit out of the existing file) and then run it through tests.
#     Test for whether the answers are as you expect by working them out by hand for comparison.
# 3 - One uses string adding, the other uses Py3.x inline variable evaluation.
# 4 - Use an Enum to define the names.