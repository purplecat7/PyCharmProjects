import datetime

from src.user import User
from src.item import Item
from src.item_list import ItemList
import nose.tools as ns

# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.

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

#####

    def test_init(self):
        print('test_init method\n')
        # Setup
        user_id = 42
        fine = 0

        # Exercise
        user = User(user_id)
        result_user_id = user.user_ID
        result_pot = user.pot
        result_item_list = user.myitems

        # Verify
        ns.assert_equal(result_user_id, user_id)
        ns.assert_equal(result_pot, fine)
        ns.assert_is_instance(result_item_list, ItemList)

        # Cleanup

    def test_find_item(self):
        print('test_find_item\n')
        # Setup
        user_id = 101
        item_title = "Can You Keep a Secret?"
        item = Item(1, "Can You Keep a Secret?")

        # Exercise
        user = User(user_id)
        user.checkout_item(item)
        item = user.find_item(item_title)
        result_item_title = item.get_title()

        # Verify
        ns.assert_is_instance(item, Item)
        ns.assert_equal(result_item_title, item_title)

        # Cleanup

    def test_total_fines(self):
        print('test_total_fines\n')
        # Setup
        user_id = 102
        total_fines = 0

        # Exercise
        user = User(user_id)
        result_total_fines = user.total_fines()

        # Verify
        ns.assert_equal(result_total_fines, total_fines)

    def test_total_borrowed(self):
        print('test_total_borrowed\n')
        # Setup
        user_id = 103
        total_borrowed = 0

        # Exercise
        user = User(user_id)
        result_total_borrowed = user.total_borrowed()

        # Verify
        ns.assert_equal(result_total_borrowed, total_borrowed)

    def test_total_overdue(self):
        print('test_total_overdue\n')
        # Setup
        user_id = 104
        total_overdue = 0

        # Exercise
        user = User(user_id)
        result_total_overdue = user.total_overdue()

        # Verify
        ns.assert_equal(result_total_overdue, total_overdue)

    def test_add_to_fine_pot(self):
        print('test_total_overdue\n')
        # Setup
        user_id = 105
        fine_to_add = 7.70

        # Exercise
        user = User(user_id)
        user.add_to_fine_pot(fine_to_add)
        result_fine = user.pot

        # Verify
        ns.assert_equal(result_fine, fine_to_add)

    def test_subtract_from_fine_pot(self):
        print('test_total_overdue\n')
        # Setup
        user_id = 106
        fine_to_add = 7.70
        fine_to_subtract = 2.30
        final_fine = 5.40

        # Exercise
        user = User(user_id)
        user.add_to_fine_pot(fine_to_add)
        user.subtract_from_fine_pot(fine_to_subtract)
        result_fine = user.pot

        # Verify
        ns.assert_almost_equal(result_fine, final_fine, 2)

    def test_remove_item(self):
        print('test_remove_item\n')
        # Setup
        user_id = 107
        item1 = Item(1, "Down Under")
        item2 = Item(2, "A Spot of Bother")
        item_title_to_remove = "Down Under"
        item_list = [item1]

        # Exercise
        user = User(user_id)
        user.checkout_item(item1)
        user.checkout_item(item2)
        user.remove_item(item_title_to_remove)
        result_item_list = user.myitems._list

        # Verify
        ns.assert_equal(result_item_list, item_list)

    def test_check_fines(self):
        print('test_check_fines\n')
        # Setup
        user_id = 108
        fine = 0.0

        # Exercise
        user = User(user_id)
        result_fine = user.pot

        # Verify
        ns.assert_almost_equal(result_fine, fine, 2)

    def test_able_to_borrow_true(self):
        print('test_check_borrowed_false\n')
        # Setup
        user_id = 109
        user_able_to_borrow = True

        # Exercise
        user = User(user_id)
        result_over_borrow_limit = user.able_to_borrow(5)

        # Verify
        ns.assert_equal(result_over_borrow_limit, user_able_to_borrow)

    def test_able_to_borrow_false(self):
        print('test_check_borrowed_true\n')
        # Setup
        user_id = 110
        user_able_to_borrow = False
        item1 = Item(1, "Down Under")
        item2 = Item(2, "A Spot of Bother")

        # Exercise
        user = User(user_id)
        user.checkout_item(item1)
        user.checkout_item(item2)
        result_over_borrow_limit = user.able_to_borrow(1)

        # Verify
        ns.assert_equal(result_over_borrow_limit, user_able_to_borrow)

    def test_check_overdue(self):
        print('test_check_overdue\n')
        # Setup
        user_id = 110
        are_overdue = True
        item = Item(1, "Down Under")

        # Exercise
        user = User(user_id)
        user.checkout_item(item, date=datetime.datetime.today() - datetime.timedelta(days=100))
        result_are_overdue = user.are_all_in_date(28)

        # Verify
        ns.assert_equal(result_are_overdue, are_overdue)

    def test_ok_to_checkout_false(self):
        print('test_ok_to_checkout_false\n')
        # Setup
        user_id = 110
        are_overdue = True
        item = Item(1, "Down Under")

        # Exercise
        user = User(user_id)
        user.checkout_item(item, date=datetime.datetime.today() - datetime.timedelta(days=100))
        result_are_overdue = user.are_all_in_date(28)

        # Verify
        ns.assert_equal(result_are_overdue, are_overdue)

    def test_ok_to_checkout_true(self):
        print('test_ok_to_checkout_true\n')
        # Setup
        user_id = 110
        are_overdue = True
        item = Item(1, "Down Under")

        # Exercise
        user = User(user_id)
        user.checkout_item(item, date=datetime.datetime.today() - datetime.timedelta(days=100))
        result_are_overdue = user.are_all_in_date(28)

        # Verify
        ns.assert_equal(result_are_overdue, are_overdue)


    # @ns.raises(KeyError)
    # def test_raise_exc_with_decorator(self):
    #     print('test_raise_exc_with_decorator method\n')
    #     a = ClassA()
    #     a.raise_exc("A message")