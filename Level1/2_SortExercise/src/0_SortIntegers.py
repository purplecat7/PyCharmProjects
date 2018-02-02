num_arr = []
# put message on user interface with instructions
print("Program which allows user to enter integer numbers to sort")
# start a 'do-while' loop e.g. while (flag==true)
keep_going = True
while keep_going:
    # ask user to enter a number or 'x', and then press 'return'
    the_input = raw_input("Please type a number, or x to end, followed by 'enter'")

    # if (input != 'x')
    if the_input != 'x':
        # store the number
        num_arr.append(int(the_input))
    # else it's an 'x'
    else:
        # get out of the loop i.e. set flag=false
        keep_going = False

# this is a little addition to the design to handle a possible boundary case
if len(num_arr) > 1:
    # sort the numbers
    num_arr.sort()
    # print to screen
    print(num_arr)
else:
    # tell the user they didn't put in enough numbers to sort
    print("You need to put more than one number in!")