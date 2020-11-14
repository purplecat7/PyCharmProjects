__author__ = 'Jane'

def my_func(the_value):
    """
    Summary of func

    Details of func inc assumptions
    :param the_value: array type of windspeeds
    :return: boolean if
    """
    if the_value == 2:
        return True
    else:
        return False

def my_other_func(val1, val2):
    return val1 + val2

def my_array_func(the_array):
    try:
        result = 1
        for num in range(0, len(the_array)):
            result = the_array[num] * result
        return result
    except TypeError as te:
        print te.message
        raise te


def main():
    if (my_func(1) == True) :
        print ('Yay, it works!')
    else:
        print ('boo')

    try:
        data=['a','b','c']
        print my_array_func(data)
    except TypeError:
        print 'User is a muppet'

if __name__ == '__main__':
    main()