__author__ = 'Jane'
"""
Use the configuration manager in PyCharm to add a new Nosetests based setup
OR
run from the command line using 'nosetests tests.py'
(http://nose.readthedocs.io/en/latest/usage.html)
"""

from some_code import functions as f
import nose.tools as ns

# It's not possible (not nicely anyway) to assign variables during setup. Setup and teardown
# are really only useful for file creation/deletion etc.
# https://stackoverflow.com/questions/10565523/how-can-i-access-variables-set-in-the-python-nosetests-setup-function
def test_my_func_true():
    result = f.my_func(2)
    ns.assert_true(result)


# TODO you can find this in the 6:TODO view pane
def test_my_func_false():
    result = f.my_func(1)
    ns.assert_false(result)


def test_my_other_func():
    result = f.my_other_func(2, 3)
    ns.assert_equals(result, 5)