# Library class, handles interactions with the great unwashed and our resplendent literature
# amg 22/03/2018

from IEA_2018_redsquirrel.src.UserCollection import UserCollection
from IEA_2018_redsquirrel.src.ItemCollection import ItemCollection
from IEA_2018_redsquirrel.src.BusinessRules import USER_ELIGIBLE_TO_BORROW


class Library(object):
    def __init__(self):
        self._user_collection = UserCollection()
        self._item_collection = ItemCollection()

    # User management
    def add_user(self, user):
        """
        Given a user object, add it to the user catalogue
        :param user: User object
        :return: User object with any system-specific parameters
        """
        return self._user_collection.add_user(user)


    def user_fine(self, user_id):
        """
        Get the total fine for a user
        :param user_id:
        :return: Numerical fine amount
        """
        return self._user_collection.get_fine(user_id)
        # TODO: Why the inconsistent naming of this method through the structure?


    def pay_fine(self, user_id, amount):
        """
        User pays off [some of] their outstanding fine total
        :param user_id:
        :param amount:
        :return: N/A
        """

        self._user_collection.pay_fine(user_id, amount)


    def able_to_borrow(self, user_id):
        """
        Return a flag indicating if the user is allowed to borrow an item, given their limits on loans and fines
        :param user_id:
        :param max_loans:
        :param max_fine:
        :return: Boolean indicating their permission to borrow something new
        """
        return self._user_collection.able_to_borrow(user_id, *USER_ELIGIBLE_TO_BORROW)


    # Catalogue management
    def add_item(self, item):
        """
        Given item object, add it to the collection
        :param item:
        :return: N/A
        """

        self._item_collection.add_item(item)


    # Borrowing management
    def is_on_loan(self, item_title):
        """
        Check whether the item title is on loan
        :param item_title:
        :return:
        """
        # Assuming there's one of every title in the library
        item = self._item_collection.get_item(item_title)
        return self._item_collection.is_on_loan(item.get_identifier())


    def user_return(self, user_id, item_id):
        """
        User returns itenm
        :param user_id: 
        :param item_id: 
        :return: 
        """

        self._user_collection.return_item(user_id, item_id)


    def user_checkout(self, user_id, item_title, date=None):
        """
        User checks out item on specified date
        :param user_id: User ID (int)
        :param item_title: Item title (str)
        :param date: checkout date (datetime)


        :return:
        """
        if self.able_to_borrow(user_id):
            item = self._item_collection.get_item(item_title)
            self._user_collection.checkout_item(user_id, item, date)
        else:
            raise Exception('User cannot borrow this')






    
    