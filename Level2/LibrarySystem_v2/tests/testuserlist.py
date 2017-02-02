from src import user_list
from src import userid_error
from src import user

from nose.tools import *


@raises(userid_error.UserIdError)
def test_find_user():

    new_user = user.User()
    new_user.set_identification(1)

    ul = user_list.UserList()
    ul.add_user(new_user)
    ul._find_user(2)