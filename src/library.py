#from user_manager import UserManager
#from item_list import ItemList
#from user_list import UserList

class LibraryController(object):
    MAX_LOANS = 5
    MAX_FINE = 50

    def __init__(self):
        pass
        #self._user_manager = UserManager()
        #self._item_list = ItemList(self)
        #self._user_list = UserList(self)

    def userCheckout(self, user_id, item_title):
        pass

    def userReturn(self, user_id, item_title):
        pass

    def userFind(self, user_id):
        pass

    def addItem(self, item):
        print(item)

    def addUser(self, user_id):
        pass
