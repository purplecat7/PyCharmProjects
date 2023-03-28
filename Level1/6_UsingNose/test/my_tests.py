import nose.tools as ns
#from src.funcs import add, open_file
import src.funcs as f

def setup_module():
    # run at start of ALL tests in this file
    pass

def teardown_module():
    # run at end of ALL tests in this file
    pass

def my_setup():
    # a test setup function
    pass

def my_teardown():
    pass

ns.with_setup(setup=my_setup, teardown=my_teardown)
def test_add():
    result = f.add(1, 2)
    ns.assert_equals(result, 3)

def test_add_wrong():
    result = f.add(3, 4)
    ns.assert_not_equals(result, 2)

@ns.raises(SystemError)
def test_open_file():
    f.open_file()