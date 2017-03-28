from item_list import ItemList
from user_list import UserList

class LibraryController(object):
    MAX_LOANS = 5
    MAX_FINE = 50

    def __init__(self):
        self._itemList = ItemList(self)
        self._userList = UserList(self)

    def userCheckout(self, userId, itemTitle):
        """Checkout an item for a user."""
        if self._userList.ableToBorrow(userId, self.MAX_LOANS, self.MAX_FINE):
            return self._itemList.checkoutItem(itemTitle)

    def userReturn(self, userId, itemTitle):
        """Return an item for a user."""
        self._userList.returnItem(userId)

    def isOnLoad(self, itemTitle):
        """Find out if an item is on load."""
        print(itemTitle)

    def payFine(self, userId, amount):
        """Pay a find for a user."""
        print(userId)
        print(amount)

    def userFind(self, userId):
        """Find a user from their ID."""
        print(userId)

    def addItem(self, item):
        """Add an item to the library."""
        print(item)

    def addUser(self, userId):
        """Add an user to the library."""
        print(userId)
