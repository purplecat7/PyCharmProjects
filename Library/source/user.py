# Object of User for library system project
# Author: Carl Haines
from item_list import ItemList

class User:

    def __init__(self, name, user_id):
        # constructor
        self.name = name
        self.user_id = user_id
        self.accrued_fine = 0
        self.max_borrow = 5
        self.max_fine = 50
        self.my_item_list = ItemList()
        # Make an instance of ItemList


    def __del__(self): # destructor
        pass


    def can_borrow(self):
        '''
        Check if user is allowed to borrow
        :return:
        '''
        len_items = self.my_item_list.len_items()# ask ItemList for length of list
        if len_items < self.max_borrow & self.accrued_fine < self.max_fine: # check length of list against max_borrow
                                                                            # Check accrued fine less than max_fine
            is_overdue = self.my_item_list.is_overdue() # Ask ItemList if any items on ItemList are overdue
            can_borrow = not is_overdue # Flip False to True and True to False
        else:
            can_borrow = False
        return can_borrow


    def checkout(self, itemid, date):
        '''
        Checkout book
        :param item:
        :param date:
        :return:
        '''

        self.my_item_list.add_to_list(itemid, date)# Ask ItemList to add item to list


    def ammend_fine(self, amount):
        '''
        add amount to self.accrued fine
        :param amount:
        :return:
        '''
        self.accrued_fine += amount


    def check_in(self, itemid):
        '''
        asks item list to check in item
        :param itemid:
        :return:
        '''
        fine = self.my_item_list.check_in(itemid)# ask itemlist to check in item
        self.accrued_fine += fine

