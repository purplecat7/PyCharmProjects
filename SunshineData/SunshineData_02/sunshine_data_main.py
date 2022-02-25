__author__ = 'Jane'
'''
Tasks:
1 - We have delegated file handling to a different module to keep things simple here - how is this done?
2 - What's less than ideal about line 37?
3 - Open file_reader.py and follow its tasks
NOTE: addition of a file header...
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
   NONE

"""
# TODO runtime options: filename, variable, operation, plot_type

import file_reader


if __name__ == '__main__':
    # set file path/name here not in the reader, so it's easier to change later
    filename = '..//MODE3_2015-08-25_2014-09-01_2015-08-25_d447917LU.csv'
    # call FileReader.loadFile(filepath) to return data in a suitable variable
    # TODO extracted_data = readfile(filename, variable_wanted)
    extracted_data = file_reader.loadfile(filename)
    # get the data to plot
    # plottable_data = process_data(extracted_data, operation)
    # send processed data to Plotting.* methods to draw graphs
    # do_plot(plottable_data, variable_name, plot_type)






# Answers:
# 1 - Function written in another module and imported
# 2 - host machine operating system specific file/folder separators
# 3 - :)