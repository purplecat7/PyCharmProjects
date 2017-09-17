"""
SELF STUDY 6:  MODEL CODE
"""

from scipy.stats.stats import pearsonr,  linregress
import numpy as np


def make_month_rainfall(filename, month):
    """
    Create a rainfall time series for a specified month from the supplied data file.
    :param filename: path-name (absolute or relative) of the file holding the data e.g. "data/lusaka_ccd_gauge.txt"
    :param month: the month for which to extract data (as a number e.g. 3 = March)
    :return: rainfall time series
    """
    # Read in the data from the file
    all_month_ts = read_in_data(filename)
    # Extract data for a given month derive the calibration parameters for the month in question
    single_month_ts = extract_month(all_month_ts, month)
    calibration_params = calibrate_data(single_month_ts)
    #  create the rainfall time series array
    rfe = make_rfe(calibration_params[0], calibration_params[1], single_month_ts[:, 2])
    return rfe


def make_monthly_calibration(filename):
    """
    Create all the monthly calibrations by extracting and calculating each month in turn.
    This is an example of a wrapper function because it 'wraps' the two functions which work on individual months.
    :param filename: path-name (absolute or relative) of the file holding the data e.g. "data/lusaka_ccd_gauge.txt"
    :return: calibration parameters
    """
    all_month_ts = read_in_data(filename)
    #  months is an array containing the months of interest for this practical
    months = np.arange(1, 12)
    #  initialize an output array
    calibration_params_all = np.zeros(shape=(12,  2))

    #  loop over months
    for i in np.arange(0,  12):
        #  extract a time series for each month
        month = months[i]
        single_month_ts = extract_month(all_month_ts,  month)
        #  carry out a calibration for the month and put the data in the output array
        calibration_params_month = calibrate_data(single_month_ts)
        calibration_params_all[i,  0] = calibration_params_month[0]
        calibration_params_all[i,  1] = calibration_params_month[1]

    #  the output is an array containing calibration parameters for each month
    return calibration_params_all


def read_in_data(filename):
    """
    Reads numerical data into a numpy array from an ascii text file
    :param filename: the fully qualified pathname of the data file
    :return: the data from the file in a numpy array
    """
    input_data = np.genfromtxt(filename)
    return input_data


def extract_month(in_data,  month):
    """
    Extracts a time series of data for a single month from an input array
    :param in_data: input array with four columns of data:  year,  month,  ccd,  rain gauge measurement
    :param month: the month for which to extract data (as a number e.g. 3 = March)
    :return: the data for the specified month
    """
    #  the monthly data is extracted by selecting every 12th row,  starting from the month of interest
    #  note that python arrays start at zero
    month_data = in_data[np.arange(month-1,  len(in_data[:, 0]), 12), :]
    return month_data


def calibrate_data(in_data):
    """
    Takes an input time series containing  ccd (dependent variable,  i.e. predictor), and gauge measurement
    (independent variable,  i.e. predictand), and uses a linear model to derive the calibration parameters.
    :param in_data: input array with four columns of data:  year,  month,  ccd,  rain gauge measurement
    :return: calibration parameters
    """
    #  slice the array to select the gauge and ccd data
    gauge = in_data[:,  3]
    ccd = in_data[:,  2]
    #  derive a linear model using the intrinsic function linregress,  imported from the scipy package
    linear_model = linregress(ccd,  gauge)
    a1 = linear_model[0]
    a0 = linear_model[1]
    #  return a tuple containing the calibration parameters
    return a0,  a1


def make_rfe(a0,  a1,  ccd):
    """
    This function makes a time series of rainfall estimates,  based on ccd observations and calibration parameters.
    :param a0: calibration parameter
    :param a1: calibration parameter
    :param ccd: observations
    :return: rainfall estimate time_series
    """
    rfe = a0 + (a1 * ccd)
    return rfe
