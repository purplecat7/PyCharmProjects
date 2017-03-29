"""LibraryController: provide a public facing interface to the library."""
from itemlist import ItemList
from userlist import UserList
import library_exceptions


class LibraryController(object):
    """Responsible for all access to objects in library

    Including all items (books, DVDs and journals), and users."""
    MAX_LOANS = 5
    MAX_FINE = 50

    def _log(self, message):
        """Poor man's 'logging'!"""
        if self._verbose:
            print(message)

    def __init__(self, verbose=True):
        """Initialize library, optionally setting verbose mode."""
        self._verbose = verbose
        self._log('Initializing {}'.format(self))
        # Initialize internal lists.
        self._item_list = ItemList()
        self._user_list = UserList()

    def add_item(self, item):
        """Add an item to the library."""
        self._log('Adding item: {}'.format(item))
        self._item_list.add_item(item)

    def add_user(self, user):
        """Add an user to the library."""
        self._log('Adding user: {}'.format(user))
        self._user_list.add_user(user)

    def is_on_loan(self, item_title):
        """Find out if an item is on load."""
        return self._item_list.is_on_loan(item_title)

    def pay_fine(self, user_id, amount):
        """Pay a find for a user."""
        self._log('Paying fine: {} - {}'.format(user_id, amount))
        self._user_list.pay_fine(user_id, amount)

    def user_checkout(self, user_id, item_title):
        """Checkout an item for a user."""
        self._log('User checkout: {} - {}'.format(user_id, item_title))
        try:
            self._user_list.able_to_borrow(user_id, self.MAX_LOANS, self.MAX_FINE)
            self._log('User {} able to borrow.'.format(user_id))
            item = self._item_list.checkout_item(item_title)
            self._user_list.checkout_item(user_id, item)
            return True
        except library_exceptions.UserNotExist:
            self._log('User {} does not exist'.format(user_id))
            return False
        except library_exceptions.FineHighError:
            self._log('User {} not able to borrow due to fine over max fine limit'.format(user_id))
            return False
        except library_exceptions.ItemDoesNotExist:
            self._log('Item {} does not exist'.format(item_title))
            return False
        except library_exceptions.TooManyItems:
            self._log('User {} not able to borrow due to many items on borrow'.format(user_id))
            return False

    def get_user_fine(self, user_id):
        """Get fines that apply to a user."""
        return self._user_list.get_fine_total(user_id)

    def user_return(self, user_id, item_title):
        """Return an item for a user."""
        self._log('User returning: {} - {}'.format(user_id, item_title))
        self._user_list.return_item(user_id, item_title)
        self._item_list.return_item(item_title)
