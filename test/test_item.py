from __future__ import print_function
from src import item
import nose.tools as ns


class TestItem:
    """Test class for Item class."""

    @classmethod
    def setup_class(cls):
        """Run once for each class before any tests are run."""
        print('setup_class')
        pass

    @classmethod
    def teardown_class(cls):
        """Run once for each class after all tests are run."""
        print('teardown_class')
        pass

    def setUp(self):
        """Run once before each test method is executed."""
        print('setUp method')
        pass

    def tearDown(self):
        """Run once after each test method is executed."""
        print('tearDown method')
        pass

    # TEST METHODS:
    def test_get_title(self):
        print('Test get_title() method')
        my_book = item.Book(1, 'The Title')
        ns.assert_equals('The Title', my_book.get_title())
        pass

    def test_get_identifier(self):
        print('Test get_identifier() method')
        my_book = item.Book(12, 'The Title')
        ns.assert_equals(12, my_book.get_identifier())
        pass

    def test_get_overdue_days(self):
        print('Test get_overdue_days() method')
        my_dvd = item.Dvd(18, 'My DVD')
        ns.assert_equals(0, my_dvd.get_overdue_days())
        pass

    def test_get_fine_due(self):
        print('Test get_fine_due() method')
        my_book = item.Book(14, 'My Book')
        ns.assert_equals(0.0, my_book.get_fine_due())
        pass

    @ns.raises(TypeError)
    def test_set_checkoute(self):
        print('Test_set_checkout() method')
        my_book = item.Book(1, 'The Title')
        my_book.set_checkout('01/01/2018')
        pass
