# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 08:54:27 2015
Note that there are runtime warnings: these must be resolved.
@author: Jane
"""
import numpy as np
import sys


def load_data(the_file):
    """
    Open the data file and load contents into memory
    :param the_file: pathname of data file
    :return: data from file in an array: storm id, windspeed and pressure
    """
    # this will open the datafile and get its contents
    # use np.genfromtxt with comments=None, delimiter=','
    the_data = np.genfromtxt(the_file, dtype=None, comments=None, delimiter=',',
                             missing_values='-999', usecols=(0, 10, 11),
                             names=('id', 'wind', 'press'))
    return the_data


def extract_field(the_data, the_field):
    """
    Function to parse the loaded data and construct a local datatype from it.
    This will be a dictionary with the storm serial number as the key, and its
    windspeeds in a list as the value.
    :param the_data: loaded data extracted from file
    :param the_field: one of 'wind' or 'press'
    :return: dictionary with storm serial number key and list of wind/press as value
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
            # append data to list unless == -999
            if item[the_field] != -999:
                data_list.append(item[the_field])
        else:
            # add old serial number and list to dictionary
            data_dict[serial_number] = data_list
            # save new serial number, append data to new list (unless -999)
            serial_number = item['id']
            if item[the_field] != -999:
                data_list = [item[the_field]]
            else:
                data_list = []
    return data_dict


def get_average_pressure_for_storm(storm_press_details):
    """
    Function which calculates the mean pressure for each storm
    :param storm_press_details: the dictionary of pressure lists by storm serial number
    :return: dictionary of mean pressure by storm serial number
    """
    # use local data to do the calculations
    avg_data = dict()
    # note that 'item' will be the key for each dictionary entry
    for item in storm_press_details:
        avg_data[item] = np.average(storm_press_details[item])
    return avg_data


def write_result(avg_dict):
    """
    Output contents of data dictionary
    :param avg_dict: dictionary of mean data by storm serial number
    :return: no return
    """
    # output result to screen
    # note - could be to file, also could be given a set of storm ids and do a plot
    for item in avg_dict:
        print ("Storm id " + item)
        print ("Mean pressure " + str(avg_dict[item]))


def main():
    # read command line arguments
    # if the file name/location is provided, get it from the command line
    if len(sys.argv) >= 2:
        the_file = sys.argv[1]
    else:
        #TODO make file path OS independent
        the_file = str("../data/ibtracs_storms.dat")

    # open data file, get data in memory
    loaded_data = load_data(the_file)

    # read data in memory and construct local datatype
    storm_wind_details = extract_field(loaded_data, 'wind')

    # read data in memory and construct local datatype
    # note that this is so similar to function to extract
    # windspeed, that we could probably use the same one but
    # parameterise which field we actually want to extract
    storm_press_details = extract_field(loaded_data, 'press')

    # process local datatype
    # note - could have user input for which storm they're interested in
    avg_press = get_average_pressure_for_storm(storm_press_details)

    # produce results
    write_result(avg_press)


if __name__ == '__main__':
    main()