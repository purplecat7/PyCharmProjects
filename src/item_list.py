from src.except_item_not_available import ItemNotAvailableError

class ItemList(list):
    """
    Class for list of library items.
    Methods (all public):
        add_item(Item): adds library item to list
        remove_item(Item): removes library item from list
        get_item(title_or_id): returns item object from item title or ID number
        get_item_from_title(title): returns item object from item title
        get_item_from_id(title): returns item object from item ID number
        checkout(Item): check item out to library user
        return(title): return item to library from use
        number_of_items(): number of items in list
        fines_owed(): total fines owed on items in list
    """

    def add_item(self, item):
        """Adds a library item to the list. Parameter: item object. No return."""
        self.append(item)

    def remove_item(self, item):
        """Remove a library item from the list. Parameter: item object. No return."""
        self.remove(item)

    def get_item_from_title(self, title):
        """
        Find library item given its title.
        Parameter: item title (str).
        Return: item object or None if title not found in list.
        """
        requested_item = None
        for item in self:
            if item.title == title:
                requested_item = item
                break
        return requested_item

    def get_item_from_id(self, item_id):
        """
        Find library item given its ID
         number.
        Parameter: item id number (int). Return: item object or None if id not found in list.
        """
        requested_item = None
        for item in self:
            if item.id == item_id:
                requested_item = item
                break
        return requested_item

    def get_item(self, item_id_or_title):
        """
        Find library item from either its title or ID number.
        Parameter: item title (str) OR item id (int).
        Return: item object.
        """
        if type(item_id_or_title) == str:
            requested_item = self.get_item_from_title(item_id_or_title)
        elif type(item_id_or_title) == int:
            requested_item = self.get_item_from_id(item_id_or_title)
        else:
            raise TypeError('Item must be identified through ID (int) or title (str)')
        return requested_item

    def return_item(self, item_id):
        """
        Check item back into library from user: remove item from item list, get final fine due on item, and tell
        item to clear checkout date.
        Parameter: item ID (int) or item title (str).
        Return: final fine owed on item (float).
        """
        returned_item = self.get_item(item_id)
        fine_due = returned_item.get_fine_due()
        returned_item.clear_checkout()
        self.remove_item(returned_item)
        return fine_due

    def checkout(self, item):
        """
        Check out library item to user: check if item available, add item to item list,
        tell item to set checkout date. Raise error if item not available to borrow.
        Parameter: item object.
        No return.
        """
        try:
            item.is_available()
            self.add_item(item)
            item.set_checkout()
        except ItemNotAvailableError:
            raise ItemNotAvailableError


    def number_of_items(self):
        """No parameters taken. Return: number of items in list."""
        list_length = len(self)
        return list_length

    def fines_owed(self):
        """No parameters taken. Return: total fines owed over all items in list (float)."""
        fine_due = 0.
        for item in self:
            fine_due += item.get_fine_due()
        return fine_due
