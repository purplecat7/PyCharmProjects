import nose.tools as ns
from src.library_manager import LibMgr
from src.userinit import UserInit

class TestUserInit(object):
    """
    Test if the library controller is the right thing to be passed on
    :param n/a
    :return n/a
    """

    def test_set_library_controller(self):
        lib_mgr = LibMgr()
        set_mgr = UserInit()
        set_mgr.set_library_controller(lib_mgr)
        test_lib_mgr = set_mgr.lib_mgr
        ns.assert_equal(lib_mgr,test_lib_mgr)