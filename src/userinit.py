class UserInit():
    """
    This is an initialization class.
    This class needs to know about the Library Manager
    and the Library Manager needs to know about this class.
    User Init class methods: allow to create a user
    that has an ID, name and surname
    """
    def __init__(self):
        pass

    def set_library_controller(theLibrary):
        """
        Two classes User Init and Library Manager
        need to know about each other
        :return:
        """
        self.LibManager = theLibrary

    def create_user(self):
        """
        Create a user with name, surname and ID.
        Allow the Library Manager to add the user to the user list
        :return:
        """
        theuser = USER("name" , "surname" , "ID")
        self.LibManager.add.user(theuser)