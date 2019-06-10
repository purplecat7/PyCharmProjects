from user_list import UserList
from item_list import ItemList

class LibrarySystem:
    
    """
    Library System Management
    """
    
    def __init__(self):
        """
        Constructor of libsys class
        """
        self.myitemlist = ItemList() #list of items
        self.myuserlist = UserList() #list of users

    def add_item(self, item):
        """
        Add item to itemlist.
        :param item: instance of item
        
        """
        self.myitemList.add_item(item)
        
    def add_user(self, user):
        """
        Add user to user list.
        :param user: instance of user
        """
        self.myuserList.add_user(user)

    def checkout(self, user, itemid):
        """
        Accepts user and id of item from input list
        and passes them to user list
        :param user: user
        :param itemid: id of iem
        :return: user, itemid
        """

        if self.myuserList.can_borrow(user):
            the_item = self.myitemlist.get_item(itemid)
            self.myuserlist.checkout_item(user, the_item)

        # JB here you need to give the user_id to the user_list so they can fin the user & check in the book
        # also might want the option to use a different date so that books can be assigned already overdue (possibly with a default value of datetime.date.today())

        return user, itemid
"""
    def return_item(self, user, itemid):

        
        Accepts user and id of item from input list
        and passes them to item initialiser
        :param user: user
        :param itemid: id of iem
        :return: user, itemid
        

        if self.myuserList.can_borrow(user):
            the_item = self.myitemlist.get_item(itemid)
            self.myuserlist.checkin_item(user, the_item)

        # JB here you need to give the user_id to the user_list so they can fin the user & check in the book
        # also might want the option to use a different date so that books can be assigned already overdue (possibly with a default value of datetime.date.today())

        return user, itemid
"""

# the following are just some ideas of methods we might want in LibSys, JB
        # feel free to delete these if it's just annoying

#return_item(user_identifier, item_identifier)
        # user_list

#change_fine_of_user(fine_reduce_by, user_identifier)

#is_item_available(item_identifier) # item identifier can be string (item_name) or integer (item_id)
        # item_list

#find_fine_of_user(user_identifier) # user identifier can be string (username) or integer (user_id)
        # etc.

#can_user_borrow(user_identifier)