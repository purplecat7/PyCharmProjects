from src.itemlist import ItemList
from src.itemSubclasses import Book
import nose.tools as ns


def test_add_item():
    item_list = ItemList()
    book = Book('Great Expectations', 1)
    item_list.add_item(book)
    ns.assert_equals(len(item_list), 1)


def test_get_identifier_id():
    book = Book('Great Expectations', 1)
    ns.assert_equals(book.get_identifier('ID'), 1)


def test_get_identifier_title():
    book = Book('Great Expectations', 1)
    ns.assert_equals(book.get_identifier('Title'), 'Great Expectations')



