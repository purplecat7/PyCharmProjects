from Level2.LibSys_2022_alexandria.src import UserList
from Level2.LibSys_2022_alexandria.src.checkout_error import NotFoundError
import nose.tools as ns

# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.

class TestUserList(object):
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

#####

    @ns.raises(NotFoundError)
    def test_find_user_not_found_error(self):
        user_list = UserList()
        user_list._find_user(2)