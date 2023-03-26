

import user
# import library_manager as m


class UserInit:
    """
    This is the user initializer class.
    This class needs to know about the Library Manager
    and the Library Manager needs to know about this class.
    -------
    Attributes:
    None
    -------
    Methods:
    set_library controller:     sets pointer to library manager
    create_user:                creates user's ID
    """
    def __init__(self):
        """
        Equivalent to the constructor. Called when class created.
        --------
        :param n/a
        :return n/a
        """
        self.lib_mgr = None     # holds pointer to library manager
        pass

    def __del__(self):
        """
        Equivalent of the destructor. Called on instance
        deletion, clears memory.
        ----------
        :param n/a
        :return n/a
        """
        pass

    def set_library_controller(self, theLibrary):
        """
        Sets pointer to the address in the memory where
        the library manager is.
        --------
        :param library manager
        :return n/a
        """
        self.lib_mgr = theLibrary

    def create_user(self, id):
        """
        Creates user's id.
        ---------
        :param ID (of the user, from main)
        :return create user's ID
        """
        theuser = user.User(id)
        self.lib_mgr.add_user(theuser)