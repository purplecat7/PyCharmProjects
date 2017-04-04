__author__ = 'Jane'

def rubbish(blob, bob, bill):
    """

    :param blob:
    :param bob:
    :param bill:
    :except ValueError
    :return:
    """
    pass


def open_netCDF_file(filename):
    """
    Given a filename, this function opens it as a NetCDF dataset.
    Function ensures file is present and throws error if not
    :param filename:
    :except ??FileNotFound
    :return: dataset
    """
    pass

def extract_field(dataset, lat, lon, fieldname):
    """
    Function to return a specific value from the dataset.
    Requires input of the lat, lon and name of field.
    Throws error on invalid field, lat or lon. Returns None if the value is missing
    :param dataset:
    :param lat:
    :param lon:
    :param fieldname:
    :except
    :return:
    """
    value = nearest_idx(dataset)
    pass

def nearest_idx(value, value_array):
    """
    search for nearest decimal degree in an array of decimal degrees and return the index.
    np.argmin returns the indices of minimum value along an axis.
    so subtract dd from all values in dd_array, take absolute value and find index of minimum.
    :param value: the value given by the user
    :param value_array: the available values
    :return: index into array of nearest value
    """
    idx = (np.abs(np.array(value_array) - float(value))).argmin()
    return idx