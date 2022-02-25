__author__ = 'Jane'
'''
Tasks
1 - investigate all the files in this project - how has the design been sketched out?
2 - note the "# TODO" special tag, can you find how it is used and where it is collected in the IDE?
3 - make sure you can run this simple code
4 - try adding some more simple types and printing them out
5 - are there any errors/warnings/issues?
'''

# don't forget to import the modules which provide the functions and access them appropriately
# e.g. import file_reader, then use file_reader.readfile() to access the function therein

if __name__ == '__main__':
    int_a = 1
    print (int_a)
    float_b = 2.0
    print(float_b)
    char_c = 'g'
    str_d = 'jwkejfkejger.kjgbj'
    print(str_d)

    # get arguments from user, possibly via command line
    # pass in arguments for the file location & name, the variable you
    # want to extract, the operation to carry out and the plot to produce.
    # call main() with the arguments
    # TODO runtime options: filename, variable, operation, plot_type

    # temporarily set file path/name here, not in the reader, so it's easier to change later

    # call FileReader.loadFile(filepath) to return data in a suitable variable
    # use functions here to process data (or if a lot, then in a processing module)
    # send processed data to Plotting.* methods to draw graphs





# Answers:
# 1 - Functionality has been gathered together, and the idea of a wrapper function for the file read
# 2 - TODO items appear on the TODO tab (View->ToolWindows->TODO)
# 3 - :)
# 4 - go on!
# 5 - nope
