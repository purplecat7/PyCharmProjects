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

    def get_fines(self, date):
        """
        ask each item what the fine is
        :param date:
        :return: total fine
        """

        pass

    def add_to_list(self, item):
        """
        adds the given item to the list
        :param item: instance of item
        :return:
        """

        pass

        self.append(item)

    def get_item(self, itemid):
        """
        returns the item asked for
        :param itemid: name of item
        :return: instance of item
        """

        if self.find_items(itemid):


    def find_items(self, itemid):
        """
        Check for item?
        :param itemid: name of item
        :return:
        """

        for item in self:
            if item.id == itemid:
                retval = True

            #ToDo: fix retval to false if the item doesn't exist

        return retval

    def check_in(self, itemid, date):
        """
        ask item to check itself in
        :param itemid:
        :param date:
        :return:
        """

        item = self.find_items(itemid)
        fine = item.checkin_item(date)

        self.remove(item)

        return fine

    def check_loan(self, itemid):
        """

        :param itemid:
        :return:
        """

        item = self.find_items(itemid)

        return item.is_onloan()
