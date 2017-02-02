from src.item_list import ItemList
from src.item_list import ItemNotFoundException
from src import item

import nose.tools as ns


class TestItemList(object):

    @ns.raises(ItemNotFoundException)
    def test_find_item(self):
        new_item = item.Book("my book", 1)
        my_list = ItemList()
        my_list.add_item(new_item)
        my_list.get_item(2)



