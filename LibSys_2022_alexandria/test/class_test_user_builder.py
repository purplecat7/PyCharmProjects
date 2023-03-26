from LibSys_2022_alexandria.src.library import Library
from LibSys_2022_alexandria.src.user import User
from LibSys_2022_alexandria.src import UserBuilder
from LibSys_2022_alexandria.src.numbid import NumbID
import nose.tools as ns
import time

# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.

class TestUserBuilder(object):
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
        print('setUp method\n Create a fresh, empty library')
        self.lib_controller = Library(5, 50)


    def tearDown(self):
        """This method is run once after _each_ test method is executed"""
        print('tearDown method\n')
        NumbID.reset_id()


    def test_init(self):
        print('test_init method\n')
        user_builder = UserBuilder()
        ns.assert_is_instance(user_builder, UserBuilder)
        ns.assert_is_none(user_builder.library)

    def test_set_library(self):
        print('test_set_library method\n')
        user_builder = UserBuilder()
        user_builder.set_library(self.lib_controller)
        ns.assert_is_instance(user_builder.library, Library)

    def test_create_user(self):
        print('test_create_user method\n')
        user_builder = UserBuilder()
        user_builder.set_library(self.lib_controller)
        user_builder.create_user()
        ns.assert_is_instance(self.lib_controller.users[0], User)
        ns.assert_equal(self.lib_controller.users[0].user_ID, 1)

    def test_create_multiple_users(self):
        print('test_create_multiple_users method\n')
        user_builder = UserBuilder()
        user_builder.set_library(self.lib_controller)
        for i in range(0, 4):
            user_builder.create_user()

        ns.assert_equal(self.lib_controller.users[0].user_ID, 1)
        ns.assert_equal(self.lib_controller.users[1].user_ID, 2)
        ns.assert_equal(self.lib_controller.users[2].user_ID, 3)
        ns.assert_equal(self.lib_controller.users[3].user_ID, 4)

    # @ns.raises(KeyError)
    # def test_raise_exc_with_decorator(self):
    #     print('test_raise_exc_with_decorator method\n')
    #     a = ClassA()
    #     a.raise_exc("A message")