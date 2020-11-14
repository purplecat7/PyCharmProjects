__author__ = 'Jane'

# This will take the file details, open it, and read the data into suitable variables to pass back

def readfile(filename, variable_wanted):
    # use 'if' statements to see what the filename extension is and then pass on the actual reading to a
    # dedicated function.
    # this is an example of a 'wrapper' function... the calling function, main(), defers responsibility to this
    # function to sort out how the file is read so doesn't need to know about different formats itself.
    # if it's csv
        # extracted_data = read_csv_file(filename, variable_wanted)
    # etc.
    return extracted_data

def read_csv_file(filename, variable_wanted):
    # do the actual donkey-work here!
    return extracted_data