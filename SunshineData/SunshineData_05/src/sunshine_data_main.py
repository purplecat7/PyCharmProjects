__author__ = 'Jane'
'''
Tasks:
1 - Make sure you understand those errors, how could they have been avoided?
2 - Experiment with setting the dtype in the data extraction to see what the effect is on the resulting stored data.
3 - See plotting.py for some more things to try
4 - Add some tests to the tests.py module
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

import numpy as np
import os
import file_reader
import plotting
import data_names as d


def add_sunshine_per_day(file_contents):
    """
    Function to iterate over hourly sunshine data and accumulate total daily hours.

    Assumes the column headings in the source data are UTC, hhmm and h.
    Converts the final result to a numpy array for easier use by calling function.

    :param file_contents: a 2D list containing date, time and data
    :return: a 2D numpy array of date and total hours per day
    """

    # We need to add up sunshine hours for each day and create a new data store to hold the results
    sunshine_hours = []

    # So first, get the first row and its date, put its sunshine hours in an accumulator
    current_date = file_contents[0][f"{d.ColNames.UTC}"]
    hours = file_contents[0][f"{d.ColNames.hrs}"]
    # loop through the data, row by row
    # we can do this with a counter for the index which goes from 2nd to the end
    # (don't forget indexes start at 0 though)
    for index in range(1, len(file_contents)):
        # Get the date, and get each subsequent one until it changes, adding up the hours as we go along
        next_date = file_contents[index][f"{d.ColNames.UTC}"]
        if next_date.date() == current_date.date():
            # ERROR 1: We don't want 'missing values' denoted by 9999.9
            if file_contents[index][f"{d.ColNames.hrs}"] < 9999.9:
                hours += file_contents[index][f"{d.ColNames.hrs}"]

    # 2 - What difference does the dtype during data extraction make?
    # Try np.int16, np.float16, np.float32 and np.float64
    # see http://docs.scipy.org/doc/numpy/user/basics.types.html for details
                print (hours)


        else:  # we've gone onto the next day
            # let's store the information in a temporary array
            temp_data = [current_date, hours]
            # and add this sub array to the main one
            sunshine_hours.append(temp_data)
            # ERROR 2: reset the accumulator - WITHOUT losing the current row's hours
            hours = file_contents[index][f"{d.ColNames.hrs}"]
            # ERROR 3: don't forget to reset the date comparison variable
            current_date = next_date

    # print(sunshine_hours)
    # print(type(sunshine_hours[0][0]))
    # funny values? see https://docs.python.org/3/tutorial/floatingpoint.html

    # And send back a numpy array of the results
    return np.array(sunshine_hours)

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
    # call FileReader.loadFile(filename) to return data in a suitable variable
    # TODO extracted_data = readfile(filename, ecv)
    file_contents = file_reader.loadfile(filename)
    # process data
    hours_per_day = add_sunshine_per_day(file_contents)
    # send processed data to Plotting.* methods to draw graphs
    plotting.plot_daily_sunshine(hours_per_day)

if __name__ == '__main__':
    # set file path/name here not in the reader, so it's easier to change later
    filename = str(
        os.getcwd() + os.sep + '..' + os.sep + '..' + os.sep + 'MODE3_2015-08-25_2014-09-01_2015-08-25_d447917LU.csv')
    main(filename)






# Answers:
# 1 - Testing
# 2 - You'll find that you get different datatypes which then take up different amounts of memory space.
# 3 - Have fun :)
# 4 - Write nosetests!