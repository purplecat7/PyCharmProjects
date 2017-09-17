"""
SELF STUDY 8:  MODEL CODE
"""
import matplotlib.pyplot as plt
from netCDF4 import Dataset
if __name__ in '__main__':
    filename = 'sst_comparisons.nc'
    in_data = Dataset(filename, 'r')
    sst_sat_1 = in_data.variables['SST_sat_1'][:]
    sst_sat_2 = in_data.variables['SST_sat_2'][:]
    moored_buoy = in_data.variables['Moored_Buoy_1'][:]
    drifter = in_data.variables['Drifting_Buoy_2'][:]
    time_1 = in_data.variables['Time_1'][:]
    time_2 = in_data.variables['Time_2'][:]
    in_data.close()
    plt.figure()
    plt.plot(time_2, drifter,  label='Drifting Buoy (1)')
    plt.plot(time_2, sst_sat_2, color='r', label='Sat SST (1)')
    plt.plot(time_1, moored_buoy, color='b', linestyle='--', label='Moored Buoy (2)')
    plt.plot(time_1, sst_sat_1, color='r', linestyle='--', label='Sat SST (2)')
    plt.xlabel('time')
    plt.ylabel('sst')
    plt.legend()
    plt.savefig('sst_comparison.png')
