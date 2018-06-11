# Beth -- 11/06/18 -- Software Development Course


class TooManyCooksError(Exception):
    """
    Raises the error for a user borrowing over their maximum allowance:
    "Each borrower can be lent up to five items"
    """

    def __init___(self):
        """
        Add to this later, if expanding this.
        :return: Nothing just yet.
        """
        pass

    def __str__(self):
        """
        New String
        :return: Returns a string to say you've borrowed over 5 items.
        """
        return "You have exceeded your maximum borrowing allowance (5 things). Give us a bloody book back before asking" \
               " for another one."
