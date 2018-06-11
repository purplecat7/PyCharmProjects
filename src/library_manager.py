# Beth -- 04/06/18 -- Software Development Course

import user_list
import item_list


class LibMgr:
    """
    Library manager - I am managing this bad-boy.
    """

    def __init__(self):
        """
        This constructor will create the item list and the user list.
        :return: A user and item list.
        """
        self.user_list = user_list.UserList()
        self.item_list = item_list.ItemList()
        # ToDo: check these amounts for fines and loans
        self.max_loans = 100
        self.max_fines = 50

    def add_item(self, item):
        """
        Adds an item to the item list.
        :param item: The item to be added to the item list.
        :return: A item list with the added item.
        """
        self.item_list.add_item(item)

    def add_user(self, user):
        """
        Adds a user to the user list.
        :param user: The user to be added to the user list.
        :return: A user list with the added user.
        """
        self.user_list.add_user(user)

    def checkout(self, ID, title, date=None):
        """
        Initialises the checkout -- to ask the item list and user list about their respective contents.
        The ID is used for the User_List, and the title is used for the Item_List.
        :param ID: The users unique identification number.
        :param title: The title of the item requested.
        :return: If able to borrow is true, it gets and checks out the item.
        """
        if self.user_list.able_to_borrow(ID, self.max_fines, self.max_loans) == True:
            the_item = self.item_list.get_item(title)
            self.user_list.checkout(ID, the_item)

    def return_item(self, ID, item_ID):
        """
        Enables a user to return an item.
        :param ID: The users unique identification number.
        :param title: The title of the returned item.
        :return: some things. # ToDo: Beth, fill this in properly.
        """
        # ToDo: add the method for return_item here
        pass

    def get_user_fines(self, ID):
        """
        Get outstanding fines owed by a user.
        :param ID: user ID number
        :return: user's outstanding fines
        """
        return self.user_list.fines_owed(ID)
