"""
SELF STUDY 3:  MODEL CODE
"""

import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap

# Note that we are no longer just writing the Python commands as a script: we have enclosed them in the special line
# if __name__ in '__main__':
# This 'script' is now a program.

if __name__ in '__main__':

    filename = './l4_sst.nc'
    data = Dataset(filename, 'r')

    print data.description
    print data.dimensions
    print data.variables
    lat = data.variables['latitude'][:]
    lon = data.variables['longitude'][:]
    sst = data.variables['sea_water_temperature'][:, :]
    uncert = data.variables['sea_water_temperature_uncertainty'][:, :]
    data.close()

    # Extract SST along the equator and along the Tropics
    sst_eq = sst[800, :]
    sst_tropic = sst[1200, :]

    # Make line plots and maps of SST
    fig = plt.figure()
    plt.plot(lon, sst_eq, label='Equator')
    plt.plot(lon, sst_tropic, '--', label='Tropics')
    plt.xlabel('Longitude / degrees')
    plt.ylabel('Sea Water Temperature / K')
    plt.legend(loc=4)
    fig.savefig("myplot1.png")
    fig_two = plt.figure()
    plt.imshow(np.flipud(sst))
    plt.title('Sea Water Temperature')
    plt.colorbar()
    plt.show()
    fig_two.savefig("myplot2.png")
    fig_three = plt.figure()
    plt.title('Sea Water Temperature')
    plt.imshow(np.flipud(sst), cmap='bwr')
    plt.colorbar()
    fig_three.savefig("myplot3.png")
    sst = sst-273.15
    fig_four = plt.figure()
    plt.title('Sea Water Temperature')
    plt.imshow(np.flipud(sst), cmap='bwr')
    plt.colorbar()
    fig_four.savefig("myplot4.png")

    # Write a netcdf file with a modified SST
    outfile = 'modified_l4_sst.nc'
    rootgrp = Dataset(outfile, mode='w')

    #  You can encourage students to add more global metadata
    rootgrp.description = 'Modified sea water temperature file from session 4 practical'
    dim_a = sst.shape[0]
    dim_b = sst.shape[1]
    rootgrp.createDimension('lat', dim_a)
    rootgrp.createDimension('lon', dim_b)
    varDims1 = ('lat', 'lon')
    var1 = rootgrp.createVariable('sst', 'f', varDims1)
    var1.units = 'Celsius'
    var1.long_name = 'Sea Water Temperature'
    var1[:, :] = sst
    rootgrp.close()

    #  Extension exercise
    fig_five = plt.figure()
    m = Basemap(projection='cea')
    x, y = m(*np.meshgrid(lon, lat))
    m.imshow(sst)
    plt.title('Sea Water Temperature')
    fig_five.savefig("myplot5.png")
