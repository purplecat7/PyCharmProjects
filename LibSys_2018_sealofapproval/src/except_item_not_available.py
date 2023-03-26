# Sharron


class ItemNotAvailableError(Exception):
    """
    Except to say that item isn't available in the lib.
    """

    def __init___(self):
        """
        Add to this later, if expanding this.
        :return: Nothing just yet.
        """
        pass

    def __str__(self):
        """
        New string
        :return: Returns a string to say that the item is not available.
        """
        return "The item requested is not available."
