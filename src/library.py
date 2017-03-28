from itemlist import ItemList
from userlist import UserList


class LibraryController(object):
    """Responsible for all access to objects in library

    Including all items (books, DVDs and journals), and users."""
    MAX_LOANS = 5
    MAX_FINE = 50

    def __init__(self):
        # Initialize internal lists.
        self._item_list = ItemList()
        self._user_list = UserList()

    def add_item(self, item):
        """Add an item to the library."""
        self._item_list.addItem(item)

    def add_user(self, user):
        """Add an user to the library."""
        self._user_list.add_user(user)

    def is_on_loan(self, item_title):
        """Find out if an item is on load."""
        return self._item_list.is_on_loan(item_title)

    def pay_fine(self, user_id, amount):
        """Pay a find for a user."""
        self._user_list.pay_fine(user_id, amount)

    def user_checkout(self, user_id, item_title):
        """Checkout an item for a user."""
        if self._user_list.able_to_borrow(user_id, self.MAX_LOANS, self.MAX_FINE):
            return self._item_list.checkout_item(item_title)
        return None

    def user_fine(self, user_id):
        """Apply a fine to a user."""
        print(user_id)

    def user_return(self, user_id, item_title):
        """Return an item for a user."""
        self._user_list.return_item(user_id)
