"""
SELF STUDY 2:  MODEL CODE
"""

import numpy as np
import matplotlib.pyplot as plt


def weather_generator(dist_mean, dist_std, num_pts):
    """
    Weather generator.
    :param dist_mean: distribution mean
    :param dist_std: distribution standard deviation
    :param num_pts: number of points
    :return: array containing a generated temperature anomaly time series
    """
    temperature_anom = np.random.normal(dist_mean, dist_std, num_pts)   # Normally distributed temperature anomaly array
    plt.plot(temperature_anom)   # Plot of time series
    plt.xlabel("Month")
    plt.ylabel("Temperature anomaly (K)")
    plt.show()
    return(temperature_anom)


def threshold_exceed(time_series, threshold):
    """
    A function for counting the number of times a threshold is exceeded in a time series
    :param time_series: time series array
    :param threshold: value against which each member of the time series is tested
    :return:  number of times the threshold is exceeded
    """
    count = 0   # Initializing the counter

    for i in np.arange(0, 100000):   # Looping over all values in the time series
        if time_series[i] > threshold:   # Testing whether the time series value is greater than the threshold
            count = count + 1   # Incrementing the counter
    return(count)      # The final value of count is returned


temperature_anomaly = weather_generator(0, 1, 10000)


switzerland_ts_historic = weather_generator(0, 0.94, 100000)
probability_2003_historic = threshold_exceed(switzerland_ts_historic, 5.1)/100000

switzerland_ts_present_meanchange = weather_generator(1.25, 0.94, 100000)
probability_2003_warm = threshold_exceed(switzerland_ts_present_meanchange, 5.1)/100000

switzerland_ts_present_meanchange_sdchange = weather_generator(1.25, 2, 100000)
probability_2003_doublesd_warm = threshold_exceed(switzerland_ts_present_meanchange_sdchange, 5.1)/100000

switzerland_ts_future = weather_generator(4.6, 2, 100000)
probability_future_2003 = threshold_exceed(switzerland_ts_future, 5.1)/100000
