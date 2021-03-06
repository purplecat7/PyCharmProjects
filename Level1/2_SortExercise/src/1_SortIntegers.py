__author__ = 'Jane'


def is_valid(candidate):
    """
    Function to check validity of user entry.
    Returns True if a valid number or 'x', False otherwise
    Can't use candidate.isdigit() as this won't work for -ve number
    :param candidate: user entered character
    :return: True if candidate is valid, false otherwise
    """
    if candidate == 'x':
        retval = True
    else:
        try:
            val = int(candidate) # cast works for +ve and -ve integers
            val += 1
            retval = True
        except ValueError as ve: # thrown if it's a float or another character
            print (ve.message)
            print(ve.args)
            retval = False
    return retval


num_arr = []
# put message on user interface with instructions
print("Program which allows user to enter integer numbers to sort")
# start a 'do-while' loop e.g. while (flag==true)
keep_going = True
while keep_going:
    # ask user to enter a number or 'x', and then press 'return'
    the_input = raw_input("Please type a number, or x to end, followed by 'enter'")
    # if it's valid i.e. it's a number or an 'x'
    if is_valid(the_input):
        # if (input != 'x')
        if the_input != 'x':
            # store the number
            num_arr.append(int(the_input))
        # else it's an 'x'
        else:
            # get out of the loop i.e. set flag=false
            keep_going = False
    # else it wasn't valid
    else:
        # tell the user
        print("Enter a number or x.")

# this is a little addition to the design to handle a possible boundary case
if len(num_arr) > 1:
    # sort the numbers
    num_arr.sort()
    # print to screen
    print(num_arr)
else:
    # tell the user they didn't put in enough numbers to sort
    print("You need to put more than one number in!")

