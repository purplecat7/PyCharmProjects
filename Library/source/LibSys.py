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
        # add for fun
        # add for fun2
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

        return user, itemid

