from __future__ import print_function
from LibSys_2018_sealofapproval.src import item
from LibSys_2018_sealofapproval.src import item_list
import nose.tools as ns
from LibSys_2018_sealofapproval.src import except_item_not_available


class TestItemList(object):
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
        self.my_list = item_list.ItemList()
        self.my_item = item.Book(34, 'Cloud Atlas')
        self.my_list.add_item(self.my_item)


    def tearDown(self):
        """This method is run once after _each_ test method is executed"""
        print('tearDown method\n')

    def test_number_of_items(self):
        print('test_number_of_items\n')
        my_second_item = item.Book(31, 'City of Stairs')
        self.my_list.add_item(my_second_item)
        ns.assert_equals(self.my_list.number_of_items(), 2)

    def test_checkout(self):
        print('test_checkout\n')
        my_user_list = item_list.ItemList()
        my_user_list.checkout(self.my_item)
        ns.assert_equals(my_user_list.number_of_items(), 1)

    @ns.raises(except_item_not_available.ItemNotAvailableError)
    def test_raise_error_not_available(self):
        print('test_raise_error_not_available\n')
        my_user_list = item_list.ItemList()
        my_user_list.checkout(self.my_item)
        another_user_list = item_list.ItemList()
        another_user_list.checkout(self.my_item)
