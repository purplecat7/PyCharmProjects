__author__ = 'Jane'
"""
see http://www.tutorialspoint.com/python/python_strings.htm
for some very useful help on strings and their methods.
"""


def is_valid(candidate):
    """
    Function to check validity of user entry.
    Returns True if any alphnumeric string, but would return False if
    decimal or -ve, so check with float cast too
    :param candidate: the user entry to check
    :return: True if a char, integer or decimal, False otherwise
    """
    if candidate.isalnum():
        if candidate.isalpha():
            retval = True, 'letter'
        else:
            retval = True, 'number'
    else:
        try:
            val = float(candidate)
            retval = True, 'number'
        except ValueError:
            retval = False, 'neither'
    return retval


the_num_arr = []
the_letter_arr = []
# put message on user interface with instructions
print("Program which allows user to enter numbers or letters to sort.")
# start a 'do-while' loop i.e. while (flag==true)
keep_going = True

while keep_going:
    # ask user to enter a number or 'space', and then press 'return'
    the_input = raw_input("Please type a number or letter, followed by 'enter'. "
                          "Use a space to end.")
    # determine type of first entry to make sure they're all the same
    valid, the_type = is_valid(the_input)
    if valid:
        if 'number' == the_type:
            the_num_arr.append(float(the_input))
        if 'letter' == the_type:
            the_letter_arr.append(the_input)
    else:
        keep_going = False


# this is a little addition to the design to handle a possible boundary case
if len(the_num_arr) > 1:
    # sort the numbers
    the_num_arr.sort()
    # print to screen
    print(the_num_arr)
if len(the_letter_arr) > 1:
    # sort the letters
    the_letter_arr.sort()
    # print to screen
    print(the_letter_arr)
else:
    # tell the user they didn't put in enough numbers/letters to sort
    print "You need to put more than one letter or number in!"

