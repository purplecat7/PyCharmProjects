# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 08:54:27 2015
This version creates one dictionary: containing both windspeed and pressure
Note that there are runtime warnings: these must be resolved.
@author: Jane
"""
import numpy as np
import sys
import os


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


def extract_fields(the_data):
    """
    Function to parse the loaded data and construct a local datatype from it.
    This will be a dictionary with the storm serial number as the key, and its
    windspeeds and pressures in a list of lists as the value. Note that the function
    expects data relating to a single storm to be contiguous.
    :param the_data: loaded data extracted from file
    :return: dictionary with storm serial number key and list of lists of wind/press as value
    """
    # create empty list and empty dictionary
    wind_list = []  # or use list()
    press_list = []  # or use list()
    data_dict = {}  # or use dict()
    # get first serial number and save it
    serial_number = the_data['id'][0]
    # for each line, get its serial number
    for item in the_data:
        # if new serial number == saved one
        if item['id'] == serial_number:
            # append data to list unless == -999
            if item['wind'] != -999:
                wind_list.append(item['wind'])
            if item['press'] != -999:
                press_list.append(item['press'])
        else:
            # add old serial number and list to dictionary
            data_dict[serial_number] = [wind_list, press_list]
            # save new serial number, append data to new list (unless -999)
            serial_number = item['id']
            if item['wind'] != -999:
                wind_list.append(item['wind'])
            else:
                wind_list = []

            if item['press'] != -999:
                press_list.append(item['press'])
            else:
                press_list = []
    return data_dict


def get_average_for_storm(storm_details, index):
    """
    Function which calculates the mean of the variable for each storm
    :param storm_details: the dictionary of variable lists by storm serial number
    :return: dictionary of mean of the variable by storm serial number
    """
    # use local data to do the calculations
    avg_data = dict()
    # note that 'item' will be the key for each dictionary entry
    try:
        for item in storm_details:
            avg_data[item] = np.average(storm_details[item])
        return avg_data
    except TypeError as te:
        #print te.message
        raise TypeError('silly user, do not use strings')


def write_result(avg_dict, variable_name):
    """
    Output contents of data dictionary
    :param avg_dict: dictionary of mean data by storm serial number
    :param variable_name: text to describe mean data
    :return: no return
    """
    # ooutput result to screen & file
    # note - could be given a set of storm ids and do a plot
    filename = "results_" + variable_name + ".txt"
    with open(filename, 'w') as text_file:
        for item in avg_dict:
            print ("Storm id: " + item)
            print ("Mean " + variable_name + ": " + str(avg_dict[item]))
            text_file.write("Storm id: {}\n".format(item))
            text_file.write("Mean {}: {}\n".format(variable_name,avg_dict[item]))


def main():
    try:
        # read command line arguments
        # if the file name/location is provided, get it from the command line
        if len(sys.argv) >= 2:
            the_file = sys.argv[1]
        else:
            #file path OS independent
            filepath = os.path.normpath("../data/ibtracs_storms.dat")
            the_file = str(filepath)

        # open data file, get data in memory
        loaded_data = load_data(the_file)

        # read data in memory and construct local datatype
        storm_details = extract_fields(loaded_data)

        # process local datatype
        # note - could have user input for which storm they're interested in
        #TODO Note that we have to hard-code the index into the dictionary to get pressure or windspeed information... this seems wrong!
        avg_wind = get_average_for_storm(storm_details, 0)

        # produce results
        write_result(avg_wind, 'windspeed')

        avg_press = get_average_for_storm(storm_details, 1)

        write_result(avg_press, 'pressure')
    except TypeError as te:
        print te.message

if __name__ == '__main__':
    main()