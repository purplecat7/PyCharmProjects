# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 08:54:27 2015

@author: Jane
"""


def load_data():
    # this will open the datafile and get its contents
    # use np.genfromtxt with comments=None, delimiter=','
    pass

def extract_windspeed():
    """
    Function to parse the loaded data and construct a local datatype from it.
    This will be a dictionary with the storm serial number as the key, and its
    windspeeds in a list as the value.
    """
    # create empty list and empty dictionary
    # get first serial number and save it and windspeed (unless -999)
    # for each line
        # get new serial number
        # if new serial number == saved one
            # append windspeed to list unless == -999
        # else
            # add old serial number and list to dictionary
            # save new serial number, append windspeed to new list (unless -999)
    pass

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
    #use sys.argv ?filename

    #open data file, get data in memory
    load_data()

    #read data in memory and construct local datatype
    extract_windspeed()

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