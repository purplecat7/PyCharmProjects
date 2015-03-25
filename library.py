"""
Definition of Library class

Author: SimonPeatman"""
__author__ = 'SimonPeatman'
import datetime


class LibraryController:
    """
    LibraryController class for LibrarySystem.

    Saves lists of items and users; handles checking out of items."""

    # parameters
    maxLoans = 5     # maximum number of loans
    maxFine = 50.0   # maximum fine (pounds)

    def __init__(self, itemList, userList):
        """
        Constructor method of Library class

        :param itemList: list of Item objects
        :param userList: list of User objects"""

        self.itemList = itemList
        self.userList = userList

    def userCheckout(self, userID, itemTitle):
        """
        Handles checking out of an item by a user.

        :param userID: unique ID of user wishing to check out item
        :param itemTitle: title of item user wishes to check out"""

        # get user object corresponding to given userID
        user = self.userList.lookup(userID)

        # get itemIDs for item currently on loan to this user
        itemIDs_loaned_list = user.getAllItems()

        # check whether user has too many items on loan already
        if not self.loanedLessThanLimit(itemIDs_loaned_list, LibraryController.maxLoans):
            print 'Too many items already on loan'
        else:

            # check whether items already on loan are overdue
            item_overdue = False
            for itemID_loaned in itemIDs_loaned_list:
                loaned_item = self.itemList.getLoanedItem(itemID_loaned)
                if loaned_item.isOverdue():
                    print 'Item %s is already overdue' % loaned_item.getTitle()
                    item_overdue = True
            if not item_overdue:

                # check whether existing fines are over the limit
                if user.isFineOverLimit(LibraryController.maxFine):
                    print 'User has fines over the limit of %s pounds' % LibraryController.maxFine
                else:

                    # get itemID of requested title
                    item_requested = self.itemList.findRequestedItem(itemTitle)
                    itemID_requested = item_requested.getID()

                    # add item to user's list and set checkout date on item itself
                    user.addItem(itemID_requested)
                    item_requested.setCheckoutDate(datetime.datetime.now())

    def loanedLessThanLimit(self, itemIDs_loaned_list, max_loans):
        """
        Returns True if the number of items currently on loan is less than the maximum.

        :param itemIDs_loaned_list: list of IDs of items on loan for one user
        :param max_loans: maximum number of simultaneous loans for one user
        :return: boolean"""

        return len(itemIDs_loaned_list) < max_loans
