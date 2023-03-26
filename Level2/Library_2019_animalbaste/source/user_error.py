

class UserError(Exception):
    """
    A class to give an error when the user is not present inside the system.

    """
    def __init__(self):

        pass

    def __str__(self):

        return 'There was an error accessing the given user. Whoever you have, they are offgrid...'