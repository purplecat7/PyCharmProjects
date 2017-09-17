"""
SELF STUDY 7:  MODEL CODE
"""
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset

if __name__ == '__main__':
    # Open the netcdf file and extract the data
    # note that this is a 'hard-coded' path which will need to be changed. It would be better to make
    # this dependency an argument into the program itself. You may like to investigate how to do this.
    filename = '/home/rg906695/extract.nc'
    fileformat = 'NETCDF3_CLASSIC'
    data = Dataset(filename, 'r', format=fileformat)

    # extract the data from the file
    bt11 = data.variables['btemp_nadir_1100'][:, :]
    ref05 = data.variables['reflec_nadir_0550'][:, :]

    # close the netcdf file
    data.close()

    # Make a set of figures of temperature and reflectance on the same plot
    fig = plt.figure()
    cmap = plt.get_cmap('Greys')
    plt.subplot(1, 2, 1)
    plt.imshow(bt11, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    plt.title('11 micron BT')
    cmap = plt.get_cmap('Greys_r')
    plt.subplot(1, 2, 2)
    plt.imshow(ref05, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    plt.title('0.55 micron reflectance')

    # Create and initialise the arrays which will hold the mask values
    mask1 = np.zeros((10, 10))
    mask2 = np.zeros((10, 10))
    mask3 = np.zeros((10, 10))

    # Use an 'if' conditional to create a mask of ones and zeros
    for elem in range(10):
        for line in range(10):
            if (bt11[elem, line] < 280):
                mask1[elem, line] = 1
            else:
                mask1[elem, line] = 0
    
    for elem in range(10):
        for line in range(10):
            if (ref05[elem, line] > 30):
                mask2[elem, line] = 1
            else:
                mask2[elem, line] = 0
    
    for elem in range(10):
        for line in range(10):
            if ((bt11[elem, line] < 280) or (ref05[elem, line] > 30)):
                mask3[elem, line] = 1
            else:
                mask3[elem, line] = 0

    # Plot the masks
    fig = plt.figure()
    cmap = plt.get_cmap('Greys_r')
    plt.subplot(1, 3, 1)
    plt.imshow(mask1, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    plt.title('Temperature Mask')
    plt.subplot(1, 3, 2)
    plt.imshow(mask2, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    plt.title('Reflectance Mask')
    plt.subplot(1, 3, 3)
    plt.imshow(mask3, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    plt.title('Combined Mask')
    plt.show()
