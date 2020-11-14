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
       Open and read a csv file given its name and location.

"""
import numpy as np
import datetime as dt


def loadfile(filename):

    """
    Reads a csv format file.

    Uses the second line of the file to name the columns. Converts fields to datetimes
    as appropriate. Expects a file containing date, time, value, value, value from line 3
    onwards. Assumes the column headings in the source data are UTC, hhmm, sec, h and W/m^2.

    :param filename: full file-path to csv file (string)
    :returns Extracted data as 2D data structure
    :raises None

    """

    convertdatefunc = lambda x: dt.datetime.strptime(x,'%Y%m%d')
    converttimefunc = lambda y: dt.datetime.strptime(y,'%H%M')
    file_contents = np.genfromtxt(filename, dtype=(dt.datetime, dt.datetime, np.int16, np.float64, np.float64),
                                  delimiter=',', skip_header=1, names=True,
                                  converters={"UTC":convertdatefunc, "hhmm":converttimefunc})
    # Send the data back to the calling function
    return file_contents
