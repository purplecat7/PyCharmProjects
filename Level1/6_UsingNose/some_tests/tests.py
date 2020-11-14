__author__ = 'Jane'
"""
Use the configuration manager in PyCharm to add a new Nosetests based setup
OR
run from the command line using 'nosetests tests.py'
(http://nose.readthedocs.io/en/latest/usage.html)
"""
# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.

from some_code import functions as f
import nose.tools as ns

def setup_module():
    print('setup_module\n')


def teardown_module():
    print('teardown_module\n')


def my_setup():
    print('my_setup called\n')


def my_teardown():
    print('my_teardown called\n')


# It's not possible (not nicely anyway) to assign variables during setup. Setup and teardown
# are really only useful for file creation/deletion etc.
# https://stackoverflow.com/questions/10565523/how-can-i-access-variables-set-in-the-python-nosetests-setup-function

# Using ns.assert*(): avoid putting in loops as it's hard to tell which loop the failure happens. Better to store
# results then compare with ideal results. If large amount of data, consider having small sub-sample.
# OK to use multiple asserts wisely as the test will tell you which one fails.
def test_my_func_true():
    print('running test_my_func_true\n')
    result = f.my_func(2)
    ns.assert_true(result)


# TODO you can find this in the 6:TODO view pane
def test_my_func_false():
    result = f.my_func(2)
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


@ns.raises(SystemExit)
def test_sys_exit():
    f.sys_exit()

@ns.with_setup(setup=my_setup, teardown=my_teardown)
def test_setup_teardown():
    print('test_setup_teardown called\n')
