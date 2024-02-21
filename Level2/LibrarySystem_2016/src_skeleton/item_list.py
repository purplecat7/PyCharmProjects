"""
NAME
    item_list - implementation of ItemList class
FILE
    item_list.py
CLASSES
    ItemList
"""


class ItemList(list):
    """
    Class to contain and manage Items, inherits list class to implement storage

    Methods defined here:

        add_item(...)
            Add an item to the list
        
        remove_item(...)
            Remove an item from the list
        
        get_item(...)
            Return an item object from the list given an identifier
        
        number_of_items(...)
            Retrieve the number of items in the list

        get_fines(...)
            Returns the accumulated fine from each overdue item.
            
        checkout_item(...)
            Adds an item being checked out to the item list

        return_item(...)
            Removes an item being checked in from the item list

        is_on_loan(...)
            Query checkout status of an item

    ----------------------------------------------------------------------
    No data or other attributes defined here.

    """
    def __init__(self):
        pass

    def __del__(self):
        pass
    
    def add_item(self, item):
        """
        Add an item object to the item list

        :param item: the object to add to the list
        :return: no return
        """
        
    def remove_item(self, item):
        """
        Remove an item object from the item list

        :param item: the object to remove from the list
        :return: no return
        """

    
    def get_item(self, identifier):
        """
        Searches for an item in the ItemList given an identifier

        :param identifier: value to uniquely identify the item, can be either:
                            Int: unique ID of the item
                            String: the title of the item
        :return: an item object matching the identifier.
        :rtype: Item
        """

        
    def number_of_items(self):
        """
        Retrieve the number of items in the list
        :return: number of items
        :rtype: int
        """


    def get_fines(self):
        """
        Accumulates the fines from each item in the list.
        Fines only accrue on overdue checked out items.
            
        :return: total fine in pounds
        :rtype: float
        """
        # Initialise the fine

        
    def checkout_item(self, item, date=False):
        """
        Adds an item to be checked out to the item list
        
        :param item: The item to be checked out
        :param date: optional, if provided then used, otherwise set to now
        :return: no return
        """


    def return_item(self, identifier):
        """
        Removes an item being checked in from the item list.

        Finds the item based on the unique identifier, then resets its checkout
        details, finally removes it from this list.
        :param identifier: value to uniquely identify the item, can be either:
                Int: unique ID of the item
                String: the title of the item
        :return: fine due on item if it's overdue
        """

    def is_on_loan(self, identifier):
        """
        Query checkout status of an item.

        Finds the item based on the unique identifier, then queries its checkout status.
        :param identifier: value to uniquely identify the item, can be either:
                Int: unique ID of the item
                String: the title of the item
        :return: True if item is on loan, False otherwise
    """


        