"""
Program to find SST for co-ordinates entered by user
Tested with netCDF4 1.1.1

Data file may be specified by argument to program.
"""
__author__ = 'Jane'

import netCDF4 as nc
import numpy as np
import os
import argparse
import configparser


def create_parser(args=None):
    """

    :return: Invocation arguments
    """
    # http://www.alanbriolat.co.uk/optional-positional-arguments-with-argparse.html
    parser = argparse.ArgumentParser(description='Data file to read contained in config file provided with -c switch.')

    # TODO make file path OS independent
    parser.add_argument('-config', '-c',
                        default=str(os.getcwd()) + '/config.ini',
                        nargs='?',
                        help="Name of configuration file to load")
    return parser.parse_args(args=args)


def read_config(config_file):
    f = open(config_file)
    configparser.ConfigParser().read_file(f)
    section = configparser.ConfigParser()['Personal']
    data_file = section.get('data_file')
    return data_file


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
    parse_args = create_parser()
    the_data_file = read_config(parse_args.config)
    # TODO check file exists before accessing
    data = nc.Dataset(the_data_file)
    # TODO remove '0' to a constants module, or parameterise
    time_idx = 0

    keep_going = True
    # TODO improve 'while' test: while keep_going, while keep_going is True, while True=keep_going
    while (keep_going == True):
        # TODO ensure only decimal lat/lon allowed
        given_lat = raw_input("Please type a latitude, or x to end, followed by 'enter'")
        if is_valid(given_lat):
            # TODO remove 'x' to a constants module, or parameterise
            if given_lat != 'x':
                given_lon = raw_input("Please type a longitude followed by 'enter'")
                # TODO check lat/lon in allowed range
                if is_valid(given_lon) and given_lon != 'x':
                    # get the SST
                    lat_idx = nearest_idx(given_lat, data.variables['lat'])
                    lon_idx = nearest_idx(given_lon, data.variables['lon'])
                    the_sst = data.variables['analysed_sst'][time_idx, lat_idx, lon_idx]
                    print the_sst
            else:
                keep_going = False
        else:
            print ("Enter a latitude or x")

if __name__ == '__main__':
    main()



