"""
File to deal with the reading of the files
"""


def read_in_time_range(file_location, file_name_format, date_range):
    """
    Read netCDF files in location to single netCDF oject
    :param file_location:
    :param file_name_format:
    :param date_range:
    :return: cube
    """

    file_list = make_file_list_time_range(file_location, file_name_format, date_range)

    # iterate over files in list to create cube

    # concatenate?

    # return cube
    pass


def make_file_list_time_range(file_location, file_name_format, date_range):
    """
    Make list of files in location according to format and date range
    :param file_location:
    :param file_name_format:
    :param date_range:
    :return: file_list
    """

    # loop over files in location matching format

    # test for date_range condition

    # return list
    pass


def save_file_time_range(file_location, file_name_format, date_range, save_location):
    """
    Optionally save concatenated file to specified location
    :param file_location:
    :param file_name_format:
    :param date_range:
    :param save_location:
    :return:
    """

    # read_file_etc

    # save
    pass