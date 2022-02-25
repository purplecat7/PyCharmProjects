__author__ = 'Jane'
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
       Open and read a file given its name and location.

"""
import numpy as np
import datetime as dt

def loadfile(filename):
    '''
    Main entry function which takes any file type and calls appropriate specific loader.
    :param: filename: full filepath to data file (string)
    :returns: loaded data as 2D array
    '''
    if str(filename).endswith('csv'):
        extracted_data = read_csv_file(filename)
    # etc.
    return extracted_data


def read_csv_file(filename):
    '''
    Function to read a csv format file.

    Uses the second line of the file to name the columns. Converts fields to datetimes
    as appropriate. Expects a file containing date, time, value, value, value, from line 3
    onwards.

    :param: filename: full filepath to csv file (string)
    :returns: 2D array of file data without header lines
    :raise: None
    '''
   # define anonymous functions to process DTG values in the source data
    convertdatefunc = lambda x: dt.datetime.strptime(x.decode("utf-8"),'%Y%m%d')
    converttimefunc = lambda y: dt.datetime.strptime(y.decode("utf-8"),'%H%M')

    # process the data file and apply conversion functions to named columns
    file_contents = np.genfromtxt(filename, dtype=(dt.datetime, dt.datetime, np.int16, np.float64, np.float64),
                                  delimiter=',', skip_header=1, names=True,
                                  converters={"UTC": convertdatefunc, "hhmm": converttimefunc})

    # Send the data back to the calling function
    return file_contents
