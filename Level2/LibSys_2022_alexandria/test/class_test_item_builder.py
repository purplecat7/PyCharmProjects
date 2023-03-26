from Level2.LibSys_2022_alexandria.src.library import Library
from Level2.LibSys_2022_alexandria.src.item_children import Book, DVD, Journal
from Level2.LibSys_2022_alexandria.src.item_builder import ItemBuilder
from Level2.LibSys_2022_alexandria.src.item_list import ItemList
from Level2.LibSys_2022_alexandria.src.numbid import NumbID
import nose.tools as ns

# Writing to stdout to record behaviour - one would never usually print from tests.
# In run configuration, need to add '--nocapture' as nosetest parameter.


class TestItemBuilder(object):
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
        item_builder = ItemBuilder()
        ns.assert_is_instance(item_builder, ItemBuilder)
        ns.assert_is_none(item_builder.file_data, None)
        ns.assert_is_none(item_builder.library, None)
        ns.assert_is_instance(item_builder.item_list, ItemList)

    def test_set_library(self):
        print('test_set_library method\n')
        item_builder = ItemBuilder()
        item_builder.set_library(self.lib_controller)
        ns.assert_is_instance(item_builder.library, Library)

    def test_load_books_in_file(self):
        print('test_load_books_in_file method\n')
        item_builder = ItemBuilder()
        item_builder.set_library(self.lib_controller)
        item_builder.load_books_in_file("../src/top100t.txt")
        ns.assert_is_instance(
            item_builder.item_list.get_item_from_title("Thermal physics of the atmosphere. 2nd edition."), Book)
        ns.assert_is_instance(
            item_builder.item_list.get_item_from_title("Harry Potter and the Prisoner of Azkaban"), Book)
        ns.assert_equal(item_builder.item_list.number_of_items(), 101)

    def test_create_book(self):
        print('test_create_book method\n')
        item_builder = ItemBuilder()
        item_builder.set_library(self.lib_controller)
        item_builder.create_book("Hi")
        ns.assert_is_instance(
            item_builder.item_list.get_item_from_title("Hi"), Book)

    def test_create_DVD(self):
        print('test_create_DVD method\n')
        item_builder = ItemBuilder()
        item_builder.set_library(self.lib_controller)
        item_builder.create_dvd("Hi")
        ns.assert_is_instance(
            item_builder.item_list.get_item_from_title("Hi"), DVD)

    def test_create_journal(self):
        print('test_create_journal method\n')
        item_builder = ItemBuilder()
        item_builder.set_library(self.lib_controller)
        item_builder.create_journal("Hi")
        ns.assert_is_instance(
            item_builder.item_list.get_item_from_title("Hi"), Journal)

    def test_populate_library(self):
        print('test_populate_library method\n')
        item_builder = ItemBuilder()
        item_builder.set_library(self.lib_controller)
        item_builder.create_journal("Hi")
        item_builder.create_dvd("Bye")
        item_builder.populate_library()

        ns.assert_is_instance(self.lib_controller.items.get_item_from_title("Hi"), Journal)
        ns.assert_is_instance(self.lib_controller.items.get_item_from_id(1), Journal)
        ns.assert_is_instance(self.lib_controller.items.get_item_from_title("Bye"), DVD)
        ns.assert_is_instance(self.lib_controller.items.get_item_from_id(2), DVD)
