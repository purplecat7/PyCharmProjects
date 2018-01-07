__author__ = 'Jane'
# don't forget to import the files which provide the functions and
# access them appropriately
# e.g. import file_reader, then use file_reader.readfile() to access the function therein

def main(filename, ecv, operation, plot_type):
    # This is an example of a docsstring - look up the PEP8 standards to find out more about all sorts
    # of Python coding standards which will make your code better.
    '''
    Function to create a plot from a data file with user specified calculations and climate variable.
    :param filename: fully qualified file name of the input data
    :param ecv: the name of the climate variable to operate on
    :param operation: the operation to carry out, may be one of 'average' or 'summation'
    :param plot_type: the type of plot to produce, may be one of 'bar', 'line' or 'pie'
    :return: no return
    '''

    # extract data
    # extracted_data = readfile(filename, variable_wanted)

    # get the data to plot
    # plottable_data = process_data(extracted_data, operation)

    # lastly, get it plotted
    # do_plot(plottable_data, variable_name, plot_type)


if __name__ == '__main__':
    # get arguments from user, possibly via command line
    # pass in arguments for the file location & name, the variable you
    # want to extract, the operation to carry out and the plot to produce.
    # call main() with the arguments