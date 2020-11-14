__author__ = 'Jane'
'''
Tasks:
1 - Note the addition of a new function to do the data processing. If it gets big and complex, it should be broken down
    and put in its own separate module.
2 - Run the program and call FileReader.loadfile1, 2 & 3 in turn. Follow the tasks in file_reader.py.
3 - Note that we now have a placeholder for calling the new processing function once we have the data loading sorted out.
    How are we able to print out some information from it?
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
# TODO runtime options
# option: have a command line switch to run tests... -t
#       (or better still, use a test framework such as 'nosetests'
# option: take file name from command line argument
import file_reader

def add_sunshine_per_day(file_contents):
    """

    :param file_contents:
    :return:
    """
    return 'add_sunshine_per_day has been called'




if __name__ == '__main__':
    # if command switch != t
        # set file path/name here not in the reader, so it's easier to change later
    filename = '..\MODE3_2015-08-25_2014-09-01_2015-08-25_d447917LU.csv'
        # call FileReader.loadFile(filepath) to return data in suitable variables
    file_contents = file_reader.loadfile1(filename)
    #file_contents = file_reader.loadfile2(filename)
    #file_contents = file_reader.loadfile3(filename)
        # use functions here to process data
    result = add_sunshine_per_day(file_contents)
    print(result)
        # send processed data to Plotting.* methods to draw graphs
    # else:
        # call methods in tests.py