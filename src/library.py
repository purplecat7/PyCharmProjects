from src.user_list import UserList
from src.item_list import ItemList
from src.checkout_error import CannotBorrowError

class Library():
    """
    A library controller
    """

    def __init__(self, max_loans, max_fines):
        # Initialises empty UserList and ItemList
        # Also set max_loans and max_fines from input
        self.users = UserList()
        self.items = ItemList()
        self.max_loans = max_loans
        self.max_fines = max_fines
        self.max_overdue = 0

    def __del__(self):
        # Removes the constructed UserList and ItemList
        self.users = None
        self.items = None

    def add_user(self, user):
        """
        Method takes User from UserBuilder and adds to the Library UserList

        Args:
            user (User): User to be added to the library
        """
        self.users.add_user(user)

    def add_items(self, items):
        """
        Method takes ItemList from ItemBuilder and adds to Library ItemList

        Args:
            items (ItemList): ItemList to be used as the Library catalogue
        """
        # TODO: add functionality to append to the Library ItemList rather than create anew
        self.items = items

    def can_checkout(self, user_id):
        """
        Method checks whether the user can checkout an item

        Args:
            user_id (float): ID of the user which wants to checkout an item
            item_title (str): Title of the item which the user wants to checkout
            max_loans (int): Maximum number of items which a user can loan
            max_fines (float): Maximum fines a user can accrue
        
        Returns:
            borrow_check (bool): Boolean of whether the user can checkout items

            :raise CannotBorrowError
        """
        try:
            borrow_check = self.users.able_to_borrow(user_id, self.max_loans, self.max_fines, self.max_overdue)
            return borrow_check
        except CannotBorrowError:
            raise
        # except NotFoundError:  # TODO
        #     raise

    def get_item(self, item_title):
        """
        Method gets an item from the Library ItemList given the item_title

        Args:
            item_title (str): Title of the item which the user wants to checkout

        Returns:
            matching_item (Item): The requested item in the Libraries ItemList
        """
        # TODO: handle the case when the item was unable to be found in the Library ItemList
        # For now, assume that the item is definitely in the Library ItemList
        matching_item = self.items.get_item_from_title(item_title)
        return matching_item

    def checkout_item(self, user_id, item_title, date=None):
        """
        Method performs checkout of the given item_title

        Args:
            user_id (float): ID of the user which wants to checkout an item
            item_title (str): Title of the item which the user wants to checkout
        """
        item = self.items.get_item_from_title(item_title)
        self.users.checkout_item(user_id, item, date=date)

    def return_item(self, user_id, item_id):
        """
        Method allows a user to return an item

        Args:
            user_id (float): ID of the user which wants to checkout an item
            item_title (str): Title of the item which the user wants to checkout
        """
        self.users.return_item(user_id, item_id)

    def get_total_fine(self, user_id):
        """
        Method gets the total current fine for the user

        Args:
            user_id (float): ID of the user which wants to request current fine
        """
        total_fine = self.users.get_fine_total(user_id)
        return total_fine

    def pay_fine(self, user_id, amount):
        """
        Method allows user to pay their current fine

        Args:
            user_id (float): ID of the user which wants to pay fine
            amount (float): The amount which the user wants to pay
        """
        self.users.pay_fine(user_id, amount)

    def check_item_availability(self, item):
        """_summary_

        Args:
            item (_type_): _description_
        """