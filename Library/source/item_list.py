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
        :return: length of self
        """

        return len(self)

    def is_overdue(self, itemid, date):
        """
        asks the item if it is overdue
        :param itemid: id of item
        :param date:
        :return: pass on message from item
        """

        pass

    def is_any_overdue(self):
        """
        loops over all items and checks if any are overdue
        :return:
        """
        retval = False
        for item in self:
            retval = retval or item.is_overdue()

        return retval

    def get_fines(self):
        """
        ask each item what the fine is
        :return: total fine
        """

        fine = 0

        for item in self:
            fine += item.calculate_fine()

        return fine

    def add_to_list(self, item):
        """
        adds the given item to the list
        :param item: instance of item
        :return:
        """

        self.append(item)

    def get_item(self, itemid):
        """
        returns the item asked for
        :param itemid: name of item
        :return: instance of item
        """

        for item in self:
            if isinstance(itemid, str):
                if item.name == itemid:
                    retval = item
            elif isinstance(itemid, int):
                if item.id == itemid:
                    retval = item

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

    def check_in(self, itemid):
        """
        ask item to check itself in
        :param itemid:
        :return:
        """

        item = self.get_item(itemid)
        fine = item.checkin_item()

        self.remove(item)

        return fine

    def check_loan(self, itemid):
        """

        :param itemid:
        :return:
        """

        item = self.get_item(itemid)

        return item.is_onloan()
