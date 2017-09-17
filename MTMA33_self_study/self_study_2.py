"""
SELF STUDY 2:  MODEL CODE
"""

import numpy as np
import matplotlib.pyplot as plt


def weather_generator(distmean, diststd, npts):
    '''Weather generator.
    Input: distribution mean,  distribution standard deviation,  number of points
    Output: array containing a generated temperature anomaly time series '''
    temperature_anom = np.random.normal(distmean, diststd, npts)   # Normally distributed temperature anomaly array
    plt.plot(temperature_anom)   # Plot of time series
    plt.xlabel("Month")
    plt.ylabel("Temperature anomaly (K)")
    plt.show()
    return(temperature_anom)

temperature_anomaly = weather_generator(0, 1, 10000)


def threshold_exceed(timeseries, threshold):
    '''A function for counting the number of times a threshold is exceeded in a time series
    Input: time series array,  threshold
    Output:  number of times the threshold is exceeded'''
    count = 0   # Initializing the counter

    for i in np.arange(0, 100000):   # Looping over all values in the time series
        if timeseries[i] > threshold:   # Testing whether the time series value is greater than the threshold
            count = count + 1   # Incrementing the counter
    return(count)      # The final value of count is returned

switzerland_ts_historic = weather_generator(0, 0.94, 100000)
probability_2003_historic = threshold_exceed(switzerland_ts_historic, 5.1)/100000

switzerland_ts_present_meanchange = weather_generator(1.25, 0.94, 100000)
probability_2003_warm = threshold_exceed(switzerland_ts_present_meanchange, 5.1)/100000

switzerland_ts_present_meanchange_sdchange = weather_generator(1.25, 2, 100000)
probability_2003_doublesd_warm = threshold_exceed(switzerland_ts_present_meanchange_sdchange, 5.1)/100000

switzerland_ts_future = weather_generator(4.6, 2, 100000)
probability_future_2003 = threshold_exceed(switzerland_ts_future, 5.1)/100000
