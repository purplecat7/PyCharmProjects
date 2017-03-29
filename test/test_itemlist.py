from src.itemlist import ItemList
from src.itemSubclasses import Book

import nose.tools as ns

def test_add_item():
    item_list = ItemList()
    book = Book('Great Expectations', 1)
    item_list.add_item(book)
    ns.assert_equals(len(item_list), 1)