__author__ = 'Jane'
"""
Use the configuration manager in PyCharm to add a new Nosetests based setup
OR
run from the command line using 'nosetests tests.py'
(http://nose.readthedocs.io/en/latest/usage.html)
"""

from some_code import functions as f
import nose.tools as ns


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

def test_my_array_func_integers():
    data=[1, 2, 3]
    result = f.my_array_func(data)
    ns.assert_equal(result, 6)

@ns.raises(TypeError)
def test_my_array_func_letters():
    data=['a','b','c']
    f.my_array_func(data)
