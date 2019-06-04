# Object of User for library system project

class User:

    def __init__(self, name, user_id):
        # constructor
        self.name = name
        self.user_id = user_id
        self.accrued_fine = 0
        self.max_borrow = 5
        self.max_fine = 50
        # Make an instance of ItemList


    def __del__(self):
        # destructor


    def can_borrow(self):
        '''
        Check if user is allowed to borrow
        :return:
        '''
        # ask UserList for length of list
        # check length of list against max_borrow
        # Check accrued fine less than max_fine
        # Ask UserList if any items are overdue


    def checkout(self, item, date=None):
        '''
        Checkout book
        :param item:
        :param date:
        :return:
        '''
        # Set the borrowing date to item
        # Ask ItemList to add item to list



