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
import stormStruct as ss


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
    This will be a list of Storm objects. Note that the function expects data relating to
    a single storm to be contiguous.
    :param the_data: loaded data extracted from file
    :return: list of Storm objects
    """
    # create empty list for Storm structures
    storm_list = []  # or use list()
    # create first Storm structure
    storm = ss.Storm()
    # get first serial number and save it in the Storm structure
    storm.stormid = the_data['id'][0]

    # for each line, get its serial number
    for item in the_data:
        # if new serial number == saved one
        if item['id'] == storm.stormid:
            # append data to structure's list unless == -999
            if item['wind'] != -999:
                storm.windspeed.append(item['wind'])
            if item['press'] != -999:
                storm.pressure.append(item['press'])
        else:
            # add old storm structure to the list
            storm_list.append(storm)
            # make a new Storm, save new serial number, append data to new list (unless -999)
            # no need to reset the lists as they are already empty in the new structure
            storm = ss.Storm()
            storm.stormid = item['id']
            if item['wind'] != -999:
                storm.windspeed.append(item['wind'])

            if item['press'] != -999:
                storm.pressure.append(item['press'])
    # add the final storm when the_data runs out
    storm_list.append(storm)
    return storm_list


def get_averages_for_storm(storms):
    """
    Function which calculates the mean of the variables for each storm
    :param storms: the list of StormClass structures
    :return: dictionary of mean of the variable by storm serial number
    """
    # Create empty dictionaries to hold results
    avg_wind_data = dict()
    avg_press_data = dict()
    # note that 'item' will be each Storm structure in the list
    try:
        for item in storms:
            avg_wind_data[item.stormid] = np.average(item.windspeed)
            avg_press_data[item.stormid] = np.average(item.pressure)
        return avg_wind_data, avg_press_data
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
    # output result to screen & file
    # note - could be given a set of storm ids and do a plot
    filename = "results_" + variable_name + ".txt"
    with open(filename, 'w') as text_file:
        for item in avg_dict:
            print ("Storm id: " + item)
            print ("Mean " + variable_name + ": " + str(avg_dict[item]))
            text_file.write("Storm id: {}\n".format(item))
            text_file.write("Mean {}: {}\n".format(variable_name,avg_dict[item]))


def main():
    # read command line arguments
    # if the file name/location is provided, get it from the command line
    if len(sys.argv) >= 2:
        the_file = sys.argv[1]
    else:
        # file path OS independent
        filepath = os.path.normpath("../data/ibtracs_storms.day")
        the_file = str(filepath)
    while True:
        try:
            if os.path.isfile(the_file):
                break
            else:
                the_file = raw_input("Please give valid file for analysis: ")
        except Exception:
            pass

    # open data file, get data in memory
    loaded_data = load_data(the_file)

    # read data in memory and construct local datatype
    storms = extract_fields(loaded_data)

    # process local datatype
    # note - could have user input for which storm they're interested in
    avg_wind, avg_press = get_averages_for_storm(storms)

    # produce results
    write_result(avg_wind, 'windspeed')

    write_result(avg_press, 'pressure')


if __name__ == '__main__':
    main()