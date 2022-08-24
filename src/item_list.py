class ItemList:

    _list = []

    def __init__(self):
        # initialise instance attributes
        self.__list = list()
        pass

    def __del__(self):
        # initialise instance attributes
        pass

    # @staticmethod

    @classmethod
    def add_item(self, title, _list):
        """ This function adds an item givem by the item builder and add it
        to the library Items List"""
        _list.aappend(title)
        pass

    def find_item(self, title):
        """ This function tries to find an item specified by the Library
        Return: Yes or No
        """
        pass

    def check_all_fines(self, ID):
        """ This function check the fines with the items
        Return: value of fines"""
        pass

    def check_overdue(self, ID):
        """ This function check the fines with the items
        Return: value of fines"""
        pass

    def add_user_list(self, title):
        """ This function add checked-out items to users item list
        Return: value of fines"""
        pass
