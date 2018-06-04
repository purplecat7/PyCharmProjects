class ItemList(list):
    """
    Class for list of library items.
    Methods:
        add_item(Item): adds library item to list
        remove_item(Item): removes library item from list
        get_item(title): returns item object from item title
        checkout(Item): check item out to library user
        return(title): return item to library from use
        number_of_items(): number of items in list
        fines_owed(): total fines owed on items in list
    """

    def __add_item(self, item):
        """Input: item object. No return. Adds a library item to the list."""
        self.append(item)

    def __remove_item(self, item):
        """Input: item object. No return. Removes a library item from the list."""
        self.remove(item)

    def get_item_from_title(self, title):
        """Input: string of item title. Return: item object or None if title not found in list."""
        requested_item = None
        for item in self:
            if item.title == title:
                requested_item = item
                break
        return requested_item

    def get_item_from_id(self, item_id):
        """Input: item id number. Return: item object or None if id not found in list."""
        requested_item = None
        for item in self:
            if item.id == item_id:
                requested_item = item
                break
        return requested_item

    def get_item(self, item_id):
        """Input: string of item title OR item id. Return: item object.
        Uses get_item_from_title if input is string and get_item_from_id if input is int."""
        if type(item_id) == str:
            requested_item = self.get_item_from_title(item_id)
        elif type(item_id) == int:
            requested_item = self.get_item_from_id(item_id)
        else:
            raise TypeError('Item must be identified through ID (int) or title (str)')
        return requested_item

    def return_item(self, item_id):
        """Input: int of item ID or string of item title. Return float: final fine owed on item.
        Check item back into library from user: remove item from item list, get final fine due on item, and tell
        item to clear checkout date."""
        returned_item = self.get_item(item_id)
        fine_due = returned_item.get_fine_due()
        returned_item.clear_checkout()
        self.remove_item(returned_item)
        return fine_due

    def checkout(self, item):
        """Input: item object. No return.
        Check out library item to user: check if item available,
        add item to item list, tell item to set checkout date. Raise error if item not available to borrow."""
        if item.is_available():
            self.add_item(item)
            item.set_checkout()
        else:
            raise KeyError('Item not available to borrow.')

    def number_of_items(self):
        """Returns number of items in list (no parameters taken)."""
        list_length = len(self)
        return list_length

    def fines_owed(self):
        """Return float: total fines owed over all items in list. No parameters taken."""
        fine_due = 0.
        for item in self:
            fine_due += item.get_fine_due()
        return fine_due
