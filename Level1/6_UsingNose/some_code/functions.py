__author__ = 'Jane'

def my_func(the_value):
    """
    Summary of func

    Details of func inc assumptions
    :param the_value: an integer to test
    :return: boolean: True if the_value is equal to 2, else False
    """
    if the_value == 2:
        return True
    else:
        return False

def my_other_func(val1, val2):
    return val1 * val2

def main():
    if (my_func(1) == True) :
        print ('Yay, it works!')
    else:
        print ('boo')

if __name__ == '__main__':
    main()