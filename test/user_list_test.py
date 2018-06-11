from src.user_list import UserList
from src.user import User
from src.user_not_valid import UserIdError
import nose.tools as ns


class TestUserList(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        cls.user_list =UserList()
        #create a couple of users for the list
        user1= User(1)
        user2=User(2)
        #add them to the list
        cls.user_list.add_user(user1)
        cls.user_list.add_user(user2)


    @ns.raises(UserIdError)
    def test_no_user(self):
        # ask for a user not on the list
        #ns.assert_raises(UserIdError, TestUserList.user_list.find(3), "ccc")
        TestUserList.user_list.find(30)

    def test_on_list(self):
        #check a user is on the list
        #i.e no exception raised when you find them
        TestUserList.user_list.find(1)

    def test_add_user(self):
        #add a user to the list
        user = User(3)
        TestUserList.user_list.add_user(user)
        #check this user is on the list
        user = TestUserList.user_list.find(3)
        #check their id returned is right
        ns.assert_equals(3,user.get_id())
