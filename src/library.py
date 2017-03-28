#from item_manager import ItemManager
#from user_manager import UserManager
#from item_list import ItemList
#from user_list import UserList

class LibraryController(object):
    MAX_LOANS = 5
    MAX_FINE = 50

    def __init__(self):
        pass
        #self._item_manager = ItemManager()
        #self._user_manager = UserManager()
        #self._item_list = ItemList(self)
        #self._user_list = UserList(self)

    def user_checkout(self, user_id, item_title):
        pass

    def user_return(self, user_id, item_title):
        pass

    def user_fin(self, user_id):
        pass

    def add_item(self, item_title):
        print(item_title)

    def add_user(self, user_id):
        pass
