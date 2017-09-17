"""
SELF STUDY 1:  MODEL CODE
"""

import numpy as np
import matplotlib.pyplot as plt


nh_years_temperature = np.genfromtxt('nh_temperature.txt')    # Reads in the northern hemisphere temperature data from the file nh_temperature.txt
years = nh_years_temperature[:, 0]    # Selects the years by selecting the first column of numbers
nh_temperature = nh_years_temperature[:, 1:13]   # Selects the temperature data by selecting columns 2 to 13 of data

annual_temp = np.mean(nh_temperature, axis=1)   # Calculates the annual mean temperature by calculating the mean over all columns of data
years_annual_temp = (years, annual_temp)    # Put the arrays into a tuple in preparation for invoking np.vstack
ts = np.vstack(years_annual_temp)    # Make a 2d array


pos_ts = np.zeros(shape=(1, 2))    # Initializing the variables
neg_ts = np.zeros(shape=(1, 2))

'''the next lines of code show a step by step approach to designing the nested loops'''

'''Using a for loop,  print out all 166 rows of your time series array to the screen in turn.  '''
for i in np.arange(0, 166):   # Looping over every row
    print(ts[:, i])   # Both columnes are plotted

'''Now using an if conditional,  rather than printing out the actual row,  print out whether the data value is positive or negative.'''

for i in np.arange(0, 166):   # Looping over every row
    if ts[1, i] >= 0:    # Testing to see if the temperature is positive
        print('Positive')
    if ts[1, i] < 0:    # Testing to see if the temperature is negative
        print('Negative')

'''Now append positive values to pos_ts and negative values to neg_ts.'''
for i in np.arange(0, 166):    # Looping through each value of the time series
    if ts[1, i] >= 0:
        tmp = np.reshape(ts[:, i], (1, 2))    # Reshaping the data into a 1 row,  2 column array
        pos_ts = np.append(pos_ts, tmp, axis=0)    # Appending to pos_ts along the first axis (row)
    if ts[1, i] < 0:
        tmp = np.reshape(ts[:, i], (1, 2))
        neg_ts = np.append(neg_ts, tmp, axis=0)


pos_ts = pos_ts[1:, :]    # Eliminating the first [[0, 0]] value of the pos_ts and neg_ts arrays
neg_ts = neg_ts[1:, :]

'''This makes a bar plot time series of temperature anomalies,  coloured red for positive and blue for negative'''
plt.bar(pos_ts[:, 0], pos_ts[:, 1], color='red')
plt.bar(neg_ts[:, 0], neg_ts[:, 1], color='blue')
plt.ylim((-1, 1))
plt.xlabel('Year')
plt.ylabel('Temperature anomaly (Kelvin)')
plt.title('Time series of annual anomalies temperature anomalies:  Northern hemisphere land')
plt.show()
