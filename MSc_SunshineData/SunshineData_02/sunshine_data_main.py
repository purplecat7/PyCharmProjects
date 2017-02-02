__author__ = 'Jane'
'''
Tasks:
1 - Note the insertion of docstrings and comments
2 - We have delegated file handling to a different module to keep things simple here - how is this done?
3 - What's less than ideal about line 45?
4 - Open file_reader.py and follow its tasks
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
   NONE

"""
# TODO runtime options
# option: have a command line switch to run tests... -t
#       (or better still, use a test framework such as 'nosetests'
# option: take file name from command line argument
import file_reader

if __name__ == '__main__':
    # if command switch != t
        # set file path/name here not in the reader, so it's easier to change later
    filename = '..\MODE3_2015-08-25_2014-09-01_2015-08-25_d447917LU.csv'
        # call FileReader.loadFile(filepath) to return data in suitable variables
    file_reader.loadfile(filename)
        # use functions here to process data
        # send processed data to Plotting.* methods to draw graphs
    # else:
        # call methods in tests.py
