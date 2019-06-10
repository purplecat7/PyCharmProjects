class libsys:
    
    """
    Library System Management
    """
    
    def __init__(self, Itemlist, UserList):
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
        myitemList.add_item(item)
        
    def add_user(self, user):
        """
        Add user to user list.
        :param user: instance of user
        """
        myuserList.add_user(user)

    def checkout(self, user, itemid):
        """
        Accepts user and id of item from input list
        and passes them to item initialiser
        :param user: user
        :param itemid: id of iem
        :return: user, itemid
        """
        # JB here you need to give the user_id to the user_list so they can fin the user & check in the book

        return user, itemid


#return_item(user_identifier, item_identifier, date = datetime.date.today())
        # check_in

#change_fine_of_user(fine_reduce_by, username = None, user_id = None)

#is_item_available(item_identifier) # item identifier can be string (item_name) or integer (item_id)

#find_fine_of_user(user_identifier, date = datetime.date.today()) # user identifier can be string (username) or integer (user_id)

#can_user_borrow(user_identifier, date = datetime.date.today())