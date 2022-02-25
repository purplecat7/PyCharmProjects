__author__ = 'Jane'
'''
Tasks:
1 - Note the addition of a new function to do the data processing. If it gets big and complex, it should be broken down
    and put in its own separate module.
2 - Follow the tasks in file_reader.py.
3 - Also we now have a placeholder for calling the new processing function once we have the data loading sorted out.
    How are we able to print out some information from it?
NOTE: rudimentary docstring, file header augmented
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


def add_sunshine_per_day(extracted_data):
    """
    Function to process the extracted data. It will sum each day's sunshine hours
    :param extracted_data: file contents accessible in a #TODO data type
    :return: summed data as a #TODO data type
    """
    return 'add_sunshine_per_day has been called'

if __name__ == '__main__':
    # set file path/name here not in the reader, so it's easier to change later
    filename = str(os.getcwd() + os.sep + '..' + os.sep + 'MODE3_2015-08-25_2014-09-01_2015-08-25_d447917LU.csv')
    # call FileReader.loadFile(filepath) to return data in a suitable variable
    # TODO extracted_data = file_reader.loadfile(filename, variable_wanted)
    extracted_data = file_reader.loadfile(filename)
    # use functions here to process data
    result = add_sunshine_per_day(extracted_data)
    print(result)
    # send processed data to Plotting.* methods to draw graphs






# Answers:
# 3 - we get it to return a string for now just to check it's wired in