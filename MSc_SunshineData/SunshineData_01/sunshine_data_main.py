__author__ = 'Jane'
'''
Tasks
1 - investigate all the files in this project - how has the design been sketched out?
2 - note the "# TODO" special tag, can you find how it is used and where it is collected in the IDE?
3 - make sure you can run this simple code
4 - try adding some more simple types and printing them out
5 - are there any errors/warnings/issues?
'''

# TODO runtime options
# option: have a command line switch to run tests... -t
#       (or better still, use a test framework such as 'nosetests'
# option: take file name from command line argument


if __name__ == '__main__':
    int_a = 1
    print (int_a)
    float_b = 2.0
    print(float_b)
    char_c = 'g'
    str_d = 'jwkejfkejger.kjgbj'
    print(str_d)
    # if command switch != t
        # set file path/name here not in the reader, so it's easier to change later
        # call FileReader.loadFile(filepath) to return data in suitable variables
        # use functions here to process data
        # send processed data to Plotting.* methods to draw graphs
    # else:
        # call methods in tests.py