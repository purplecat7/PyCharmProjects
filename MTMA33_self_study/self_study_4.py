"""
SELF STUDY 4:  MODEL CODE
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import random


def assess_flood_risk_obsdata(filename, threshold):
    '''Assess the risk of flood based on an observed rainfall time series
    Inputs:  name of the file holding the observed time series,  threshold for a flood
    Output:  risk of a 'flood day' '''
    obs_timeseries = readindata("data/ghana_rainfall.txt")   # Read in data
    flood_risk = flood_risk_timeseries(obs_timeseries, threshold)   # Calculate the flood risk in the observed data
    return(flood_risk)


def assess_flood_risk_stochastic(filename, threshold, lengthts):
    '''Assess the risk of flood based on a stochastic rainfall time series
    Inputs:  name of the file holding the observed time series,  threshold for a flood,  length of simulated time series
    Output:  risk of a 'flood day' '''
    obs_timeseries = readindata("data/ghana_rainfall.txt")   # Read in data
    obs_stats = calculate_statistics(obs_timeseries)      # Calculate the underlying statistics of the weather
    sim_timeseries = gen_timeseries(obs_stats, lengthts)   # Generate a time series based on these statistics
    flood_risk = flood_risk_timeseries(sim_timeseries, threshold)   # Calculate flood risk in the simulated data
    return(flood_risk)


def readindata(file):
    '''Opens a file named by the user and puts the data into an array
    Input:  file name (full path)
    Output:  array containing the data contained in the file'''
    timeseries = np.loadtxt(file)
    return(timeseries)


def calculate_statistics(timeseries):
    '''Calculates the statistics of rainfall from a timeseries
    Input:  One dimensional time series array
    Output: An array of length 4 containing the following:
    [probability of rain given rain the day before,  probability of rain given
    no rain the day before,  mean rainfall amount,  standard deviation rainfall amount] '''
# initialising the variables
    count_rr = 0
    count_nr = 0
    count_nn = 0
    count_rn = 0
    rainydays = 1
# At each point in the time series,  we count dry/wet days where there has/hasn't been rainfall the day before.
    for i in np.arange(1, len(timeseries)):
        if ((timeseries[i] > 0) & (timeseries[i-1] > 0)):
            count_rr = count_rr + 1
        if ((timeseries[i] == 0) & (timeseries[i-1] > 0)):
            count_nr = count_nr + 1
        if ((timeseries[i] == 0) & (timeseries[i-1] == 0)):
            count_nn = count_nn + 1
        if ((timeseries[i] > 0) & (timeseries[i-1] == 0)):
            count_rn = count_rn + 1
        if (timeseries[i] > 0):
            rainydays = np.append(timeseries[i], rainydays)
# Based on the counts in the previous part of the code,  we calculate prr (probability of rain given rain the day before)
# and prn (probability of rain given no rain the day before).
# Note that in order for this to work,  we must have from __future__ import division at the top of the file.
# otherwise,  we run into problems of rounding to the nearest integer (eg 1/3 = 0)
    prr = count_rr/(count_rr + count_nr)
    prn = count_rn/(count_rn + count_nn)
    meanrain = np.mean(rainydays)
    sdrain = np.std(rainydays)
    return([prr, prn, meanrain, sdrain])


def gen_timeseries(stats, length_ts):
    '''Generates a time series with user defined rainfall statistics
    Inputs:  an array of rainfall statistics in the form output by calculate_statistics [probability of rain given rain the day before,  probability of rain given no rain the day before,  mean rainfall amount,  standard deviation rainfall amount],  length of time series to be generated
    Output:  an array of the generated time series'''
# assign the elements of the array to the probabilities.
    prr = stats[0]
    prn = stats[1]
    meanrain = stats[2]
    sdrain = stats[3]
# initialize arrays for the generated intensity and occurrence
    gen_intensity = np.zeros(length_ts)
    gen_occurrence = np.zeros(length_ts)
# Derive rainfall occurrence and intensity on day one. The rainfall occurrence is arbitrary.
    gen_intensity[0] = random.gauss(meanrain, sdrain)
    if random.random() > 0.5:
        gen_occurrence[0] = 1
    if random.random() <= 0.5:
        gen_occurrence[0] = 0
    for i in np.arange(1, length_ts):
        # generate the intensity for each point in time
        gen_intensity[i] = np.abs(random.gauss(meanrain, sdrain))
        # generate the occurrence at each point in time
        if ((gen_occurrence[i-1] > 0) & (random.random() < prr)):
            gen_occurrence[i] = 1
        if ((gen_occurrence[i-1] > 0) & (random.random() > prr)):
            gen_occurrence[i] = 0
        if ((gen_occurrence[i-1] == 0) & (random.random() < prn)):
            gen_occurrence[i] = 1
        if ((gen_occurrence[i-1] == 0) & (random.random() > prn)):
            gen_occurrence[i] = 0
    outts = gen_occurrence * gen_intensity
    return(outts)


def flood_risk_timeseries(timeseries, threshold=75, days=5):
    '''counts the number of times a threshold is breached and outputs the risk of the
    threshold being breached.
    Inputs:  time series array,  rainfall threshold,  days of accumulation
    Output:  Probability of a flood being in progress'''
# initialise the flood counter array
    count_floods = np.zeros(len(timeseries))
# loop over the time series putting changing the 0 in the counter array to 1 if the threshold is breached
    for i in np.arange(days, len(timeseries), days):    # Looping over time series
        if (np.sum(timeseries[i-days:i]) > threshold):    # Testing whether cumulative rainfall is greater than the threshold
            count_floods[i] = 1   # Changing the counter array element from zero to 1
# the number of breaches is the sum of count_floods array.
# Calculating the probability that a day is a flood
    return(np.sum(count_floods)/len(timeseries))
