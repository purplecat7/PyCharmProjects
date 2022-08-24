from src.userlist import UserList
from src.itemlist import ItemList

class Library():

    def __init__(self, max_loans, max_fines):
        # Initialises empty UserList and ItemList
        # Also set max_loans and max_fines from input
        self.users = UserList()
        self.items = ItemList()
        self.max_laons = max_loans
        self.max_fines = max_fines

    def __del__(self):
        # Removes the constructed UserList and ItemList
        self.users = None
        self.items = None

    def add_users(self, users):
        # Method takes UserList from UserBuilder and adds to the Library UserList
        pass

    def add_items(self, items):
        # Method takes ItemList from ItemBuilder and adds to Library ItemList
        pass

    def checkout_item(self, user_id, item):
        # Method allows a User to checkout an Item if allowed
        pass

    def return_item(self, user_id, item):
        # Method allows a User to return an Item
        pass

    def find_user(self, user_id):
        # Method finds a User from the Library UserList from the given user_id.
        # Returns the found User
        pass

    def get_total_fine(seld, user_id):
        # Method gets the total fine from a User
        pass

    def pay_fine(self, user_id, amount):
        # Method allows User to pay an amount of their fine
        pass