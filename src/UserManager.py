class UserManager:
    # Q: What is a "manager" thing?
    # Q: Should be called "UserCollectionManager"?

    def set_library_controller(self, library_controller):
        # Q: Why set a library controller? Shouldn't I manage a UserCollection?
        raise NotImplementedError

    def create_user(self, user_id):
        # From the UML
        raise NotImplementedError
