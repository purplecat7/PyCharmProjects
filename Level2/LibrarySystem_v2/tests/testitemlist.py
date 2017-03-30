from ..src.item_list import ItemList
from ..src.item_list import ItemNotFoundException
from ..src import item

import nose.tools as ns


def test_add_item():
    item_list = ItemList()
    book = item.Book('The Tao of Pooh', 1)
    item_list.add_item(book)
    ns.assert_equals(len(item_list), 1)


def test_get_identifier_id():
    book = item.Book('The Tao of Pooh', 1)
    ns.assert_equals(book.get_identifier('ID'), 1)


def test_get_identifier_title():
    book = item.Book('The Tao of Pooh', 1)
    ns.assert_equals(book.get_identifier('Title'), 'The Tao of Pooh')


def test_get_item_ID():
    item_list = ItemList()
    book = item.Book('The Tao of Pooh', 1)
    item_list.add_item(book)
    ns.assert_equals(book, item_list.get_item(1))


def test_get_item_title():
    item_list = ItemList()
    book = item.Book('The Tao of Pooh', 1)
    item_list.add_item(book)
    ns.assert_equals(book, item_list.get_item('The Tao of Pooh'))


class TestItemList(object):
    @ns.raises(ItemNotFoundException)
    def test_find_item(self):
        new_item = item.Book("my book", 1)
        my_list = ItemList()
        my_list.add_item(new_item)
        my_list.get_item(2)



