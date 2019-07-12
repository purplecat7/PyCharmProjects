from invalid_item_error import InvalidItemError

class ItemList(list):
    """
    This is a list that holds a number of items
    methods:
    len_items()
    is_overdue(item)
    add_to_list()
    get_item()
    find_items()
    """
    def len_items(self):
        """
        number of items in the list
        :return: int
        """

        return len(self)

    # def is_overdue(self, itemid, date):
    #     """
    #     asks the item if it is overdue
    #     :param itemid: id of item
    #     :param date:
    #     :return: nothing
    #     """
    #
    #     pass

    def is_any_overdue(self):
        """
        loops over all items and checks if any are overdue
        :return: bool
        """
        retval = False
        for item in self:
            retval = retval or item.is_overdue()

        return retval

    def get_fines(self):
        """
        ask each item what the fine is
        :return: float
        """

        fine = 0

        for item in self:
            fine += item.calculate_fine()

        return fine

    def add_to_list(self, item):
        """
        adds the given item to the list
        :param item: instance of item
        :return: nothing
        """

        self.append(item)

    def get_item(self, itemid):
        """
        returns the item asked for
        :param itemid: name of item
        :return: instance of item
        """

        retval = None

        for item in self:
            if isinstance(itemid, str):
                if item.name == itemid:
                    retval = item
            elif isinstance(itemid, int):
                if item.id == itemid:
                    retval = item

        if retval is None:
            raise InvalidItemError

        return retval

    # def find_items(self, itemid):
    #     """
    #     Check for item?
    #     :param itemid: name of item
    #     :return:
    #     """
    #
    #     retval = False
    #
    #     for item in self:
    #         retval = retval & item.id == itemid
    #
    #     return retval

    def check_out(self, item, date=None):
        """

        :param item: instance of an item
        :param date: date to set as
        :return: nothing
        """

        item.setdate(date)
        self.append(item)


    def check_in(self, itemid):
        """
        ask item to check itself in
        :param itemid:
        :return: float
        """

        item = self.get_item(itemid)
        fine = item.checkin_item()

        self.remove(item)

        return fine

    def check_loan(self, itemid):
        """

        :param itemid:
        :return: bool
        """

        item = self.get_item(itemid)

        return item.is_onloan()
