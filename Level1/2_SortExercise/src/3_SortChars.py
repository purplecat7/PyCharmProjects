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
        retval = True
    else:
        try:
            val = float(candidate)
            retval = True
        except ValueError:
            retval = False
    return retval


the_arr = []
# put message on user interface with instructions
print("Program which allows user to enter numbers or letters to sort. All entries must be the"
      "same type as the first")
# start a 'do-while' loop i.e. while (flag==true)
keep_going = True
numbers = False
letters = False
while keep_going:
    # ask user to enter a number or 'space', and then press 'return'
    the_input = raw_input("Please type a number, letter, or space to end, followed by 'enter'")
    # determine type of first entry to make sure they're all the same
    if is_valid(the_input):
        if the_input.isalpha():
            letters = True
        else:
            numbers = True
        if numbers and not letters:
            the_arr.append(float(the_input))
        if letters and not numbers:
            the_arr.append(the_input)
        if letters and numbers:
            print("You cannot mix letters and numbers. Program terminating.")
            exit()

    else:
        keep_going = False


# this is a little addition to the design to handle a possible boundary case
if len(the_arr) > 1:
    # sort the numbers
    the_arr.sort()
    # print to screen
    print(the_arr)
else:
    # tell the user they didn't put in enough numbers to sort
    print("You need to put more than one number in!")

