

import user
#import library_manager as m

class UserInit():
    """
    This is an initialization class.
    This class needs to know about the Library Manager
    and the Library Manager needs to know about this class.
    User Init class methods: allow to create a user
    that has an ID, name and surname
    """
    def __init__(self):
        self.lib_mgr = None     # holds pointer to library manager
        pass

    def set_library_controller(self, theLibrary):
        """
        Two classes User Init and Library Manager
        need to know about each other
        :return:
        """
        self.lib_mgr = theLibrary

    def create_user(self, id):
        """
        Create a user with name, surname and ID.
        Allow the Library Manager to add the user to the user list
        :return:
        """
        theuser = user.User(id)
        self.lib_mgr.add_user(theuser)