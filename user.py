class User():
    """
    Class to create user for
    the library application
    """

    def __init__(self):
        self._identification = str()
        self._first_name = str()
        self._last_name = str()
        self._total_items = int()
        self._items = list()

    def __del__():
        pass

    @property
    def identification(self):
        """
        Gets the user id
        """
        return self._identification

    @identification.setter
    def identification(self, value):
        """
        Sets the user id
        """
        self._identification(value)

    @property
    def first_name(self):
        """
        Gets the user first name
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Sets the user first name
        """
        self._first_name(value)

    @property
    def last_name(self):
        """
        Gets the user last name
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Sets the user last name
        """
        self._last_name(value)

    @property
    def total_items(self):
        """
        Gets the total user items
        """
        return self._total_items

    @total_items.setter
    def _total_items(self):
        """
        Sets the total user items
        """
        self._total_items(len(self._items)

    @property
    def items(self):
        """
        Gets the user associated items
        """
        pass

    @items.setter
    def items(self, value):
        """
        Sets the user items
        """
        pass
