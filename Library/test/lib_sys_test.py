from class_code.classAcode import ClassA
import nose.tools as ns
from library_system import LibrarySystem
import time

# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.

class TestA(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        # ns.assert_true(False, "setup_class run")
        print('setup_class\n')

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""
        # ns.assert_true(False, "teardown_class run")
        print('teardown_class\n')


    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        # use self.attribute to keep anything which needs to be accessed later
        print('setUp method\n')


    def tearDown(self):
        """This method is run once after _each_ test method is executed"""
        print('tearDown method\n')


    def test_init(self):
        print('test_init method\n')
        lib_sys = LibrarySystem()
        ns.assert_is_instance(self.myitemlist, list)
        ns.assert_is_instance(self.myuserlist, list)

    def test_return_true(self):
        print('test_return_true method\n')
        libsys = LibrarySystem()
        ns.assert_equal(libsys.return_true(), True)
        ns.assert_not_equal(libsys.return_true(), False)

    def test_raise_exc(self):
        print('test_raise_exc method\n')
        libsys = LibrarySystem()
        ns.assert_raises(KeyError, libsys.raise_exc, "Lib Sys value")

    @ns.raises(KeyError)
    def test_raise_exc_with_decorator(self):
        print('test_raise_exc_with_decorator method\n')
        libsys = LibrarySystem()
        libsys.raise_exc("Library System message")