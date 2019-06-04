# Object of User for library system project

class User:
    #class attributes

    def __init__(self, name, user_id):
        # constructor
        self.name = name
        self.user_id = user_id
        self.max_borrow = 5
        self.max_fine = 50
        # Make an instance of ItemList


    def __del__(self):
        # destructor

    def lenitems(self):
        '''
        Ask ItemList for length of list
        :return: length int
        '''
        pass

    def is_overdue(self):
        '''
        Ask ItemList if any item is overdue
        :return: Boolean
        '''
        pass

    def set_date(self, item):
        '''
        Set the borrowed date on an item
        :param item:
        :return: item
        '''
        pass

    def add_to_list(self, item):
        '''
        Ask ItemList to add item to list
        :param item:
        :return:
        '''
        pass

