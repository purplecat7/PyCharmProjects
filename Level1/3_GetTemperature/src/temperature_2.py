"""
Script to find SST for co-ordinates entered by user
Tested with netCDF4 1.1.1
"""
__author__ = 'Jane'

import netCDF4 as nc
import numpy as np

def isValid(the_input):
    """
    Function to check validity of user entry.
    Returns True if a digit or 'x', False otherwise
    """
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


data = nc.Dataset("/home/jane/Documents/06_ReSC_data/20100601120000-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_LT-v02.0-fv01.0.nc")
time_idx = 0

keep_going = True
while (keep_going == True):
    given_lat = input("Please type a latitude, or x to end, followed by 'enter'")
    if isValid(given_lat):
        if given_lat != 'x':
            given_lon = input("Please type a longitude followed by 'enter'")
            if isValid(given_lon) and given_lon != 'x':
                # get the SST
                lat_idx = nearest_idx(given_lat, data.variables['lat'])
                lon_idx = nearest_idx(given_lon, data.variables['lon'])
                the_sst = data.variables['analysed_sst'][time_idx, lat_idx, lon_idx]
                print(the_sst)
        else:
            keep_going = False
    else:
        print ("Enter a latitude or x")




