"""
Program to find SST for co-ordinates entered by user
Tested with netCDF4 1.1.1

Data file may be specified on command line.
"""
__author__ = 'Jane'

import netCDF4 as nc
import numpy as np
import sys


def is_valid(the_input):
    """
    Function to check validity of user entry.
    Returns True if a digit or 'x', False otherwise
    """
    # TODO remove 'x' to a constants module, or parameterise
    if the_input == 'x':
        retval = True

    # TODO this check possibly doesn't work for float and/or -VE, use try/except
    # elif input.isdigit():
    #    retval = True

    else:
        try:
            # TODO check whether casting down to int always raises error
            val = int(the_input)
            retval = True
        except ValueError:
            try:
                val = float(the_input)
                retval = True
            except ValueError:
                retval = False
    return retval


def nearest_idx(value, value_array):
    """
    search for nearest decimal degree in an array of decimal degrees and return the index.
    np.argmin returns the indices of minimum value along an axis.
    so subtract dd from all values in dd_array, take absolute value and find index of minimum.
    :param value: the value given by the user
    :param value_array: the available values
    :return: index into array of nearest value
    """
    idx = (np.abs(np.array(value_array) - float(value))).argmin()
    return idx


def main():
    # if the file name/location is provided, get it from the command line
    if len(sys.argv) >= 2:
        the_file = sys.argv[1]
    else:
        # TODO make file path OS independent
        the_file = str("/home/jane/Documents/06_ReSC_data/20100601120000-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_LT-v02.0-fv01.0.nc")
    # TODO check file exists before accessing
    # my_file=open(the_file)
    data = nc.Dataset(the_file)
    # TODO remove '0' to a constants module, or parameterise
    time_idx = 0

    keep_going = True
    # TODO improve 'while' test: while keep_going, while keep_going is True, while True=keep_going
    while (keep_going == True):
        # TODO ensure only decimal lat/lon allowed
        given_lat = input("Please type a latitude, or x to end, followed by 'enter'")
        if is_valid(given_lat):
            # TODO remove 'x' to a constants module, or parameterise
            if given_lat != 'x':
                given_lon = input("Please type a longitude followed by 'enter'")
                # TODO check lat/lon in allowed range
                if is_valid(given_lon) and given_lon != 'x':
                    # get the SST
                    lat_idx = nearest_idx(given_lat, data.variables['lat'])
                    lon_idx = nearest_idx(given_lon, data.variables['lon'])
                    the_sst = data.variables['analysed_sst'][time_idx, lat_idx, lon_idx]
                    print(f"The sst for your location is {the_sst}")
            else:
                keep_going = False
        else:
            print ("Enter a latitude or x")


if __name__ == '__main__':
    main()



