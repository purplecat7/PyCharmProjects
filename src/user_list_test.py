from user_list import Userlist
import nose.tools as ns

class TestUserList(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""

        #create a couple of users for the list