__author__ = 'Jane'
'''
Tasks:
1 - Check out the matpotlib help and gallery. Add a axis labels, sort out the x-axis labels, and make the dots
    different shapes/colours.
2 - If you have time, try putting values into histogram bins... perhaps how many days are in each bin of low, medium
    or high hours (limits to be set by you and put on the plot)
'''
# -------------------------------------------------------------------------------
# Name:        Plotting
# Purpose:     Demonstration for MSc welcome week
#
# Author:      Jane Lewis xw904346
#
# Created:     25/08/2015
# Copyright:   (c) xw904346 2015
# -------------------------------------------------------------------------------

"""
NAME
   Plotting - Given data, generate plots
FILE
   plotting.py

FUNCTIONS
   plot_daily_sunshine(...)
       Open and read a csv file given its name and location.

"""

import matplotlib.pyplot as plt
import matplotlib.dates

def plot_daily_sunshine(sunshine_hours):
    # let's do a simple graph but look at http://matplotlib.org/gallery.html for ideas
    dates = matplotlib.dates.date2num(sunshine_hours[:,0])
    plt.plot_date(dates, sunshine_hours[:,1])
    plt.axes()
    plt.title('Daily sunshine hours')
    plt.show()