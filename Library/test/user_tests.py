import nose.tools as ns
from ..source.user import User


class TestUser(object):
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
        user = User('Jackson', 15)
        ns.assert_equal('Jackson', user.name)
        ns.assert_equal(user.user_id, 15)
        ns.assert_equal(user.accrued_fine, 0)
        ns.assert_equal(user.max_fine, 50)
        ns.assert_equal(user.max_borrow, 5)

    def test_can_borrow(self):
        pass

    def test_checkout(self):
        pass

    def test_amend_fine(self):
        pass

    def test_check_in(self):
        pass

    



