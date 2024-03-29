#from class_code.classAcode import ClassA
import nose.tools as ns
from ..source.library_system import LibrarySystem
import time

# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.

class TestLibSys(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        # ns.assert_true(False, "setup_class run")
        pass

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""
        # ns.assert_true(False, "teardown_class run")
        pass


    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        # use self.attribute to keep anything which needs to be accessed later
        pass


    def tearDown(self):
        """This method is run once after _each_ test method is executed"""
        pass


    def test_init(self):
        print('test_init method\n')
        lib_sys = LibrarySystem()
        ns.assert_is_instance(lib_sys.myitemlist, list)
        ns.assert_is_instance(lib_sys.myuserlist.available_users, list)

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