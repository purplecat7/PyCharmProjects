class UserIdError(Exception):
    """
    This is an exception class for when the user ID is not valid.
    -------
    Methods:
    -------
    Attributes:

    """

    def __init__(self, arg):
        self.message = arg

    def __str__(self):
        # repr() returns a string representation of the object
        return repr(self.message)