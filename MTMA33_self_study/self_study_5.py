"""
SELF STUDY 5:  MODEL CODE
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import random


def assess_flood_risk_perturbed(filename, threshold, lengths, perturbation):
    """
    Assess flood risk in a changed climate.
    Example of usage:  out = assess_flood_risk_perturbed("data/ghana_rain.txt", 100, 100000, np.array([0.5, 1, 2, 1]))

    :param filename: path-name of the file holding the observed time series e.g. "data/ghana_rainfall.txt"
    :param threshold: threshold for a flood
    :param lengths:  length of simulated time series
    :param perturbation:  array containing the perturbation factors
    :return: tuple containing : the new statistics,  the simulated time series,  the flood risk
    """
    obs_time_series = read_in_data(filename)   # Read in data
    obs_stats = calculate_statistics(obs_time_series)      # Calculate the underlying statistics of the weather
    new_stats = obs_stats*perturbation   # Calculate the new statistics
    sim_time_series = gen_time_series(new_stats, lengths)   # Generate a time series based on these statistics
    flood_risk = flood_risk_time_series(sim_time_series, threshold)   # Calculate flood risk in the simulated data
    return((new_stats, sim_time_series, flood_risk))


def assess_flood_risk_obsdata(filename, threshold):
    """
    Assess the risk of flood based on an observed rainfall time series
    :param filename: path-name of the file holding the observed time series e.g. "data/ghana_rainfall.txt"
    :param threshold: threshold for a flood
    :return: risk of a 'flood day
    """
    obs_time_series = read_in_data(filename)   # Read in data
    flood_risk = flood_risk_time_series(obs_time_series, threshold)   # Calculate the flood risk in the observed data
    return(flood_risk)


def assess_flood_risk_stochastic(filename, threshold, lengths):
    """Assess the risk of flood based on a stochastic rainfall time series
    :param filename: path-name of the file holding the observed time series e.g. "data/ghana_rainfall.txt"
    :param threshold: threshold for a flood
    :param lengths:  length of simulated time series
    :return:  risk of a 'flood day'
    """
    obs_time_series = read_in_data(filename)   # Read in data
    obs_stats = calculate_statistics(obs_time_series)      # Calculate the underlying statistics of the weather
    sim_time_series = gen_time_series(obs_stats, lengths)   # Generate a time series based on these statistics
    flood_risk = flood_risk_time_series(sim_time_series, threshold)   # Calculate flood risk in the simulated data
    return(flood_risk)
    

def read_in_data(filename):
    """
    Opens a file named by the user and puts the data into an array
    :param filename:  file name (absolute or relative path)
    :return: array containing the data contained in the file
    """
    time_series = np.loadtxt(filename)
    return(time_series)


def calculate_statistics(time_series):
    """
    Calculates the statistics of rainfall from a time series
    :param time_series: One dimensional time series array
    :return: An array of length 4 containing the following:
            [probability of rain given rain the day before,
            probability of rain given no rain the day before,
            mean rainfall amount,
            standard deviation rainfall amount]
    """
    # initialising the variables
    count_rr = 0
    count_nr = 0
    count_nn = 0
    count_rn = 0
    rainy_days = 1
    # At each point in the time series,  we count dry/wet days where there has/hasn't been rainfall the day before.
    for i in np.arange(1, len(time_series)):
        if ((time_series[i] > 0) & (time_series[i-1] > 0)):
            count_rr = count_rr + 1
        if ((time_series[i] == 0) & (time_series[i-1] > 0)):
            count_nr = count_nr + 1
        if ((time_series[i] == 0) & (time_series[i-1] == 0)):
            count_nn = count_nn + 1
        if ((time_series[i] > 0) & (time_series[i-1] == 0)):
            count_rn = count_rn + 1
        if (time_series[i] > 0):
            rainy_days = np.append(time_series[i], rainy_days)

    # Based on the counts in the previous part of the code,  we calculate prr (probability of rain given rain the day before)
    # and prn (probability of rain given no rain the day before).
    # Note that in order for this to work,  we must have from __future__ import division at the top of the file.
    # otherwise,  we run into problems of rounding to the nearest integer (eg 1/3 = 0)
    prr = count_rr/(count_rr + count_nr)
    prn = count_rn/(count_rn + count_nn)
    mean_rain = np.mean(rainy_days)
    sd_rain = np.std(rainy_days)
    return([prr, prn, mean_rain, sd_rain])


def gen_time_series(stats, length_ts):
    """
    Generates a time series with user defined rainfall statistics
    :param stats:  an array of rainfall statistics in the form
            [probability of rain given rain the day before,
            probability of rain given no rain the day before,
            mean rainfall amount,
            standard deviation rainfall amount]
    :param length_ts: length of time series to be generated
    :return:  an array of the generated time series
    """
    # assign the elements of the array to the probabilities.
    prr = stats[0]
    prn = stats[1]
    mean_rain = stats[2]
    sd_rain = stats[3]

    # initialize arrays for the generated intensity and occurrence
    gen_intensity = np.zeros(length_ts)
    gen_occurrence = np.zeros(length_ts)

    # Derive rainfall occurrence and intensity on day one. The rainfall occurrence is arbitrary.
    gen_intensity[0] = random.gauss(mean_rain, sd_rain)
    if random.random() > 0.5:
        gen_occurrence[0] = 1
    if random.random() <= 0.5:
        gen_occurrence[0] = 0

    for i in np.arange(1, length_ts):
        # generate the intensity for each point in time
        gen_intensity[i] = np.abs(random.gauss(mean_rain, sd_rain))
        # generate the occurrence at each point in time
        if ((gen_occurrence[i-1] > 0) & (random.random() < prr)):
            gen_occurrence[i] = 1
        if ((gen_occurrence[i-1] > 0) & (random.random() > prr)):
            gen_occurrence[i] = 0
        if ((gen_occurrence[i-1] == 0) & (random.random() < prn)):
            gen_occurrence[i] = 1
        if ((gen_occurrence[i-1] == 0) & (random.random() > prn)):
            gen_occurrence[i] = 0
    out_ts = gen_occurrence * gen_intensity
    return(out_ts)


def flood_risk_time_series(time_series, threshold=75, days=5):
    """
    Counts the number of times a threshold is breached and outputs the risk of the threshold being breached.
    :param time_series:  time series array,
    :param threshold: rainfall threshold which defaults to 75 if no value is provided
    :param days: days of accumulation which defaults to 5 if no value is provided
    :return:  Probability of a flood being in progress
    """
    # initialise the flood counter array
    count_floods = np.zeros(len(time_series))

    # loop over the time series putting changing the 0 in the counter array to 1 if the threshold is breached
    for i in np.arange(days, len(time_series), days):    # Looping over time series
        if (np.sum(time_series[i-days:i]) > threshold):    # Test whether cumulative rainfall is greater than the threshold
            count_floods[i] = 1   # Change the counter array element from zero to 1

    # the number of breaches is the sum of count_floods array.
    # Calculating the probability that a day is a flood
    return(np.sum(count_floods)/len(time_series))