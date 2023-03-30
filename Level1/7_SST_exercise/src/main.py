"""
main
"""

import reading
import plotting
import processing

def main(file_location, file_name_format, date_range, save_location_file, lat, lon, variable_name, plot_title, xlab, ylab, save_location_plot):
    """
    Oh my
    :param file_location:
    :param file_name_format:
    :param date_range:
    :param save_location_file:
    :param lat:
    :param lon:
    :param variable_name:
    :param plot_title:
    :param xlab:
    :param ylab:
    :param save_location_plot:
    :return:
    """

    cube = reading.read_in_time_range(file_location, file_name_format, date_range)

    variable = processing.slicer_lat_lon(lat, lon, variable_name, cube)

    plotting.timeseries_1var(variable, plot_title, xlab, ylab, save_location_plot)

    pass


if __name__ == '__main__':
    a = 3
    main(a, a, a, a, a, a, a, a, a, a, a)