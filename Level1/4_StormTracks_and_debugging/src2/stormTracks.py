# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 08:54:27 2015

@author: Jane
"""
import numpy as np
import sys


def load_data(the_file):
    """
    Open the data file and load contents into memory
    :param the_file: pathname of data file
    :return:
    """
    # this will open the datafile and get its contents
    # use np.genfromtxt with comments=None, delimiter=','
    the_data = np.genfromtxt(the_file, dtype=None, comments=None, delimiter=',',
                             missing_values='-999', usecols=(0, 10, 11),
                             names=('id', 'wind', 'press'))
    return the_data


def extract_windspeed(the_data):
    """
    Function to parse the loaded data and construct a local datatype from it.
    This will be a dictionary with the storm serial number as the key, and its
    windspeeds in a list as the value.
    :param the_data: loaded data extracted from file
    """
    # create empty list and empty dictionary
    data_list = []  # or use list()
    data_dict = {}  # or use dict()
    # get first serial number and save it
    serial_number = the_data['id'][0]
    # for each line, get its serial number
    for item in the_data:
        # if new serial number == saved one
        if item['id'] == serial_number:
            # append windspeed to list unless == -999
            if item['wind'] != -999:
                data_list.append(item['wind'])
        else:
            # add old serial number and list to dictionary
            data_dict[serial_number] = data_list
            # save new serial number, append windspeed to new list (unless -999)
            serial_number = item['id']
            if item['wind'] != -999:
                data_list = [item['wind']]
            else:
                data_list = []
    return data_dict


def extract_pressure():
    pass

def get_average_pressure_for_storm():
    # use local data to do the calculations
    pass

def write_result():
    # output result to screen
    # note - could be to file, also could be given a set of storm ids and do a plot
    pass


def main():
    #read command line arguments
    # if the file name/location is provided, get it from the command line
    if len(sys.argv) >= 2:
        the_file = sys.argv[1]
    else:
        # TODO make file path OS independent
        the_file = str("../data/ibtracs_storms.dat")

    #open data file, get data in memory
    loaded_data = load_data(the_file)

    #read data in memory and construct local datatype
    storm_wind_details = extract_windspeed(loaded_data)

    #read data in memory and construct local datatype
    #note that this is so similar to function to extract
    #windspeed, that we could probably use the same one but
    #parameterise which field we actually want to extract
    extract_pressure()

    #process local datatype
    #note - could have user input for which storm they're interested in
    get_average_pressure_for_storm()

    #produce results
    write_result()




if __name__ == '__main__':
    main()