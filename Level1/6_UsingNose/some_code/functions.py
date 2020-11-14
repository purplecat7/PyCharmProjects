__author__ = 'Jane'


def my_double(x):
    # Doubles the input value
    return 2*x


def my_multiply(x, y):
    # Multiplies the input values together
    return x*y


def my_double2(x):
    # Uses the my_multiply function to double the input value
    return my_multiply(x, 2)


def is_multiple_of_3(x):
    # Checks if the remainder when dividing x by 3 is zero
    # Alternatively, refactor to use the 'is_multiple_of()' generic function
    #    return is_multiple_of(x, 3)
    return (x % 3) == 0


def is_multiple_of(x, n):
    # Checks if the remainder when dividing x by n is zero
    return (x % n) == 0


def my_func(the_value):
    # Below is a docstring
    """
    Summary of function

    Details of function including assumptions...
    :param the_value: an integer to test
    :return: boolean: True if the_value is equal to 2, else False
    """
    if the_value == 2:
        return True
    else:
        return False

def my_other_func(val1, val2):
    return val1 * val2

def sys_exit():
    raise SystemExit

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

    print my_func('ducks')
    print my_double2('hello')
    print is_multiple_of('piglets', 4)

if __name__ == '__main__':
    main()