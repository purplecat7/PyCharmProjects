"""
Script to find SST for given co-ordinates
Tested with netCDF4 1.1.1
"""
__author__ = 'Jane'

import netCDF4 as nc
import numpy as np

def nearest_idx(value, value_array):
   """
     search for nearest decimal degree in an array of decimal degrees and return the index.
     np.argmin returns the indices of minimum value along an axis.
     so subtract dd from all values in dd_array, take absolute value and find index of minimum.
    """
   idx = (np.abs(np.array(value_array) - value)).argmin()
   return idx


data = nc.Dataset("C:/Users/xw904346/Documents/06_ReSC_data/20100601120000-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_LT-v02.0-fv01.0.nc")
print data.dimensions
print data.variables

given_lat = -38
given_lon = -178

# these lines find out how big the dimensions are i.e. the data's resolution
lat_dims = len(data.dimensions['lat'])
lon_dims = len(data.dimensions['lon'])
print lat_dims
print lon_dims

lat_idx = nearest_idx(given_lat, data.variables['lat'][:])
lon_idx = nearest_idx(given_lon, data.variables['lon'][:])
time_idx = 0
print lat_idx
print lon_idx

the_sst = data.variables['analysed_sst'][time_idx, lat_idx, lon_idx]

print ("SST is ")
print (the_sst)