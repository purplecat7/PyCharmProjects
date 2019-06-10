# Object of User for library system project
from item_list import ItemList

class User:

    def __init__(self, name, user_id):
        # constructor
        self.name = name
        self.user_id = user_id
        self.accrued_fine = 0
        self.max_borrow = 5
        self.max_fine = 50
        # Make an instance of ItemList
        pass


    def __del__(self):
        # destructor
        pass


    def can_borrow(self):
        '''
        Check if user is allowed to borrow
        :return:
        '''
        len_items = ItemList.len_items()# ask ItemList for length of list
        if len_items < self.max_borrow & self.accrued_fine<self.max_fine:# check length of list against max_borrow
                                                                            # Check accrued fine less than max_fine
            can_borrow = ItemList.is_overdue()# Ask ItemList if any items on ItemList are overdue TODO ask Laura if ITemList.is_overdue() checks all items in itemlist or just one
        else:
            can_borrow = False
        return can_borrow


    def checkout(self, item, date=None):
        '''
        Checkout book
        :param item:
        :param date:
        :return:
        '''
        # Set the borrowing date to item
        # Ask ItemList to add item to list
        pass



