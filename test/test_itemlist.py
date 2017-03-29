from src.itemlist import ItemList
from src.itemSubclasses import Book
from src.item import Item
from datetime import datetime

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


def test_get_item_str():
    identifier = 'Great Expectations'
    item_list = ItemList()
    book = Book('Great Expectations', 1)
    item_list.add_item(book)
    item = item_list.get_item(identifier)
    ns.assert_equals(item, book)


def test_get_item_ID():
    item = ItemList().get_item(1)
    ns.assert_equals(item, ItemList().add_item(Book('Great Expectations', 1)))


def test_checkout_date():
    date = datetime.now()
    checkout_date = Item().set_checkout(date)
    ns.assert_equals(checkout_date, date)