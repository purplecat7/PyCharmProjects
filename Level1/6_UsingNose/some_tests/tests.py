__author__ = 'Jane'
"""
Use the configuration manager in PyCharm to add a new Nosetests based setup
OR
run from the command line using 'nosetests tests.py'
(http://nose.readthedocs.io/en/latest/usage.html)
"""

from some_code import functions as f
import nose.tools as ns

def setup_module():
    f = open('test_log.txt', 'w')
    f.write('setup_module\n')
    f.close()


def teardown_module():
    f = open('test_log.txt', 'a')
    f.write('teardown_module\n')
    f.close()


def my_setup():
    f = open('test_log.txt', 'a')
    f.write('my_setup called\n')
    f.close()


def my_teardown():
    f = open('test_log.txt', 'a')
    f.write('my_teardown called\n')
    f.close()


# It's not possible (not nicely anyway) to assign variables during setup. Setup and teardown
# are really only useful for file creation/deletion etc.
# https://stackoverflow.com/questions/10565523/how-can-i-access-variables-set-in-the-python-nosetests-setup-function

# Using ns.assert*(): avoid putting in loops as it's hard to tell which loop the failure happens. Better to store
# results then compare with ideal results. If large amount of data, consider having small sub-sample.
# OK to use multiple asserts wisely as the test will tell you which one fails.
def test_my_func_true():
    result = f.my_func(2)
    ns.assert_true(result)


# TODO you can find this in the 6:TODO view pane
def test_my_func_false():
    result = f.my_func(1)
    ns.assert_false(result)


def test_my_other_func():
    result = f.my_other_func(2, 3)
    ns.assert_equals(result, 6)


@ns.raises(SystemExit)
def test_sys_exit():
    f.sys_exit()

@ns.with_setup(setup=my_setup, teardown=my_teardown)
def test_setup_teardown():
    f = open('test_log.txt', 'a')
    f.write('test_setup_teardown called\n')
    f.close()
