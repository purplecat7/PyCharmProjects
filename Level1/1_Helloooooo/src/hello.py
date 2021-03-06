"""
File: hello.py
Illustrate basic control flow and mutable function argument.
"""

import random as rd


def do_a_loop(the_message):
    """
    Function to illustrate logic of loop control
    :param the_message:
    :return: no return
    """
    my_var = rd.randint(1, 5)
    for count in range(my_var):
        print (the_message)


def do_a_decision(the_random_number):
    """
    Function to illustrate logic of decision control
    :param the_random_number:
    :return: decision result
    """
    if the_random_number <= 5.0:
        return 'small decision'
    else:
        return 'big decision'


def do_a_while():
    """
    Function to illustrate logic of do-while control
    :return: iterations achieved
    """
    count = 0
    flag = True
    the_limit = rd.randint(1, 10)
    while flag:
        count += 1
        if count >= the_limit:
            flag = False
    return count


def do_a_repeat_until():
    """
    Function to illustrate logic of repeat_until control
    :return: iterations achieved
    """
    count = 0
    the_limit = rd.randint(1, 10)
    while count <= the_limit:
        count += 1
    return count


def foobar(arg_string="abc", arg_list=[]):
    """
    Function to illustrate mutable data
    :param arg_string: input string. Default is "abc"
    :param arg_list: input array. Default is empty array
    :raise IndexError: if stupid vslue
    :return:
    """
    print("string arg: "+ arg_string + "\t\tlist arg: " + str(arg_list))
    arg_string = arg_string + "xyz"
    arg_list.append("F")


###########################################
def main():
    """
    Program to exercise various control structures.
    """
    do_a_loop('hello from loopy')
    print (do_a_decision(rd.randint(0, 10)))
    count_result = do_a_while()
    print 'while result: ' + str(count_result)
    count_result = do_a_repeat_until()
    print 'repeat_until result: ' + str(count_result)
    for i in range(4):
        foobar()

############################################
if __name__ == '__main__':
    main()
